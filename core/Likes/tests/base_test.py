class BaseLikeTestCase(object):
    MODEL_CLASS = None

    def test_is_liked(self):
        obj = self.MODEL_CLASS.create(is_liked=None)
        self.assertIsNone(obj.is_liked)

        obj.like()
        self.assertTrue(obj.is_liked)

        obj.dislike()
        self.assertFalse(obj.is_liked)

        obj.deactivate()
        self.assertIsNone(obj.is_liked)
