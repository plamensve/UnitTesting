from unittest import TestCase, main
from project.social_media import SocialMedia

class TestSocialMedia(TestCase):
    def setUp(self):
        self.social_media = SocialMedia("test_user", "Instagram", 10000, "photo")

    def test_correct_init(self):
        self.social = SocialMedia('Plamen', 'Instagram', 100, 'Test')
        self.assertEqual('Plamen', self.social._username)
        self.assertEqual('Instagram', self.social._platform)
        self.assertEqual(100, self.social.followers)
        self.assertEqual('Test', self.social._content_type)

    def test_create_post(self):
        self.assertEqual(self.social_media.create_post("Test post"),
                         "New photo post created by test_user on Instagram.")
        self.assertEqual(len(self.social_media._posts), 1)

    def test_comment_on_post(self):
        self.social_media.create_post("Test post")

        self.assertEqual(self.social_media.comment_on_post(0, "This is a comment."),
                         "Comment added by test_user on the post.")

        self.assertEqual(self.social_media.comment_on_post(0, "Short"), "Comment should be more than 10 characters.")

        self.assertRaises(IndexError, self.social_media.comment_on_post, 1, "This is a comment.")

    def test_invalid_platform(self):
        with self.assertRaises(ValueError):
            SocialMedia("test_user", "Facebook", 10000, "photo")

    def test_negative_followers(self):
        with self.assertRaises(ValueError):
            self.social_media.followers = -100

    def test_like_post_reach_limit(self):
        self.social_media.create_post("Test post")
        for _ in range(10):
            self.social_media.like_post(0)
        self.assertEqual(self.social_media.like_post(0), "Post has reached the maximum number of likes.")
        self.assertEqual(self.social_media._posts[0]['likes'], 10)

    def test_like_post_invalid_index(self):
        self.assertEqual(self.social_media.like_post(1), "Invalid post index.")

    def test_create_post_max_likes(self):
        self.social_media.create_post("Test post")
        for _ in range(10):
            self.social_media.like_post(0)
        self.assertEqual(len(self.social_media._posts), 1)

    def test_validate_and_set_platform_invalid_message(self):
        invalid_platform = 'Facebook'
        with self.assertRaises(ValueError) as context:
            self.social_media._validate_and_set_platform(invalid_platform)

        expected_error_message = f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']"
        self.assertEqual(str(context.exception), expected_error_message)

# ----------------------------------------

    def test_followers_setter_negative_value(self):
        with self.assertRaises(ValueError) as context:
            self.social_media.followers = -100

        expected_error_message = "Followers cannot be negative."
        self.assertEqual(str(context.exception), expected_error_message)


if __name__ == '__main__':
    main()
