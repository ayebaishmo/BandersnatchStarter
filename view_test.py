import unittest
import altair as alt
from pandas import DataFrame
from app.graph import chart


class TestAltairChart(unittest.TestCase):

    def setUp(self):
        """Set up a sample DataFrame for testing."""
        self.df = DataFrame({
            "Level": [1, 2, 3],
            "Health": [100, 90, 80],
            "Energy": [50, 60, 70],
            "Sanity": [90, 85, 80],
            "Rarity": ["Common", "Rare", "Legendary"]
        })
        self.x = "Level"
        self.y = "Health"
        self.target = "Rarity"

    def test_chart_properties(self):
        """Test that the chart is created with the correct properties."""
        visual = chart(self.df, x=self.x, y=self.y, target=self.target)

        self.assertIsInstance(visual, alt.Chart, "should be Altair object.")

        chart_json = visual.to_dict()

        expect_title = f"{self.y} by {self.x} for {self.target}"
        self.assertEqual(chart_json["title"], expect_title, "Title incorrect.")

        self.assertEqual(
            chart_json["encoding"]["x"]["field"],
            self.x, "X-axis incorrect.")
        self.assertEqual(
            chart_json["encoding"]["y"]["field"],
            self.y, "Y-axis incorrect.")

    def test_chart_dimensions(self):
        """Test that the chart has the correct width and height."""
        width = 400
        height = 600

        visual = chart(self.df, x=self.x, y=self.y, target=self.target)

        chart_json = visual.to_dict()

        self.assertEqual(chart_json["width"], 
                         width, "Chat width incorrect.")
        self.assertEqual(chart_json["height"], height,
                        "Chat height incorrect.")

    def test_chart_title_padding(self):
        """Test that the chart title has the correct padding."""
        visual = chart(self.df, x=self.x, y=self.y, target=self.target)

        chart_json = visual.to_dict()

        self.assertEqual(chart_json["config"]["title"]["offset"], 20,
                        "Title offset is incorrect.")


if __name__ == "__main__":
    unittest.main()
