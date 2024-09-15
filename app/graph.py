# from altair import Chart
from pandas import DataFrame
import altair as alt


def chart(df: DataFrame, x: str, y: str, target: str):
    """
    Creates an Altair chart based on the provided DataFrame and
    parameters

    Args:
    df (DataFrame): The DataFrame containing the data to be visualized.
    x (str): The column name for the x-axis.
    y (str): The column name for the y-axis.
    target (str): The column name for the color encoding.

    Returns:
    chart: The Altair chart object.
    """
    w = 400
    h = 600
    title = f"{y} by {x} for {target}"
    properties = {
        "width": w,
        "height": h,
        "background": "#2b2b2b",
        "padding": {"left": 70, "top": 70, "right": 70, "bottom": 70},
        "title": title
    }

    visual = alt.Chart(df).mark_circle().encode(
        x=alt.X(x, title=x),
        y=alt.Y(y, title=y),
        color=alt.Color(target, title=target),
        tooltip=[x, y, target]
    ).properties(**properties).configure_axis(
        labelColor='#fff',
        titleColor="#fff",
        gridColor='#888',
        gridOpacity=0.2
    ).configure_title(
        fontSize=24,
        color='#888',
        offset=20
    ).configure_legend(
        labelColor='#888888',
        titleColor='#888888'
    ).configure_view(
        stroke='#888'
    ).configure_axisLeft(
        domainColor='#888',
        domainWidth=1
    ).configure_axisTop(
        domainColor='#888'
    )

    return visual
