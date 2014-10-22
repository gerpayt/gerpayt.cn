
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction

from models import WorkCate, WorkItem


def create_work_cate(title, link, introduction=None, add_time=None, sort=None, other_info=None):
    return WorkCate.objects.create(title=title, link=link, introduction=introduction, add_time=add_time,
                                   sort=sort, other_info=other_info)


def create_work_item(title, link, category, introduction=None, add_time=None, sort=None, other_info=None):
    return WorkItem.objects.create(title=title, link=link, category=category, introduction=introduction,
                                   add_time=add_time, sort=sort, other_info=other_info)


class WorkCateViewTests(TestCase):
    def test_index_view_with_no_work_cate(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('works:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No work cate are available.")
        self.assertQuerysetEqual(response.context['work_cate_list'], [])

    def test_index_view_with_a_work_cate(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page
        """
        create_work_cate(title='title', link='link')
        response = self.client.get(reverse('works:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertContains(response, "link")
        self.assertQuerysetEqual(
            response.context['work_cate_list'],
            ['<WorkCate: %s>' % 'title']
        )

    def test_index_view_with_two_work_cate(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page
        """
        create_work_cate(title='title1', link='link1')
        create_work_cate(title='title2', link='link2')
        response = self.client.get(reverse('works:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title1")
        self.assertContains(response, "link1")
        self.assertContains(response, "title2")
        self.assertContains(response, "link2")
        self.assertQuerysetEqual(
            response.context['work_cate_list'],
            ['<WorkCate: %s>' % 'title1',
             '<WorkCate: %s>' % 'title2']
        )

    def test_index_view_with_two_same_work_cate(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page
        """
        create_work_cate(title='same_title', link='same_link')
        try:
            with transaction.atomic():
                create_work_cate(title='same_title', link='same_link')
            self.assertEqual(True, False)
        except IntegrityError:
            self.assertEqual(True, True)
        response = self.client.get(reverse('works:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "same_title")
        self.assertContains(response, "same_link")
        self.assertQuerysetEqual(
            response.context['work_cate_list'],
            ['<WorkCate: %s>' % 'same_title']
        )

    def test_cate_view_with_error_work_cate_id(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        create_work_cate(title='title', link='link')
        response = self.client.get(reverse('works:cate', args=('not-exist',)))
        self.assertEqual(response.status_code, 404)

    def test_cate_view_with_no_work_item(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        work_cate = create_work_cate(title='title', link='link')
        response = self.client.get(reverse('works:cate', args=(work_cate.link,)))
        self.assertContains(response, 'title')
        self.assertContains(response, 'The cate has no work items.')

    def test_cate_view_with_work_items(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        work_cate = create_work_cate(title='title', link='link')
        create_work_item(title='title1', link='link1', category=work_cate)
        create_work_item(title='title2', link='link2', category=work_cate)
        response = self.client.get(reverse('works:cate', args=(work_cate.link,)))
        self.assertContains(response, 'title')
        self.assertContains(response, 'title1')
        self.assertContains(response, 'title2')
