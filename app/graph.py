# from altair import Chart
from pandas import DataFrame
import altair as alt


def chart(df: DataFrame, x: str, y: str, target: str, width:int = 400, height: int = 600):
    """
    Creates an Altair chart based on the provided Datafrane and
    parameters
    
    Args:
    df (DataFrame): The Datafrane congtaining the data to be visualised.
    x (str): The colum name for the x-axis.
    y (str): The column name foy the y- axis.
    target )str) The column name for the color encoding.

    returns:
    chart: The ALtair chart object
    """

    title = f"{y} by {x} for {target}"
    properties = {
        "width": width,
        "height": height,
        "background": "#2b2b2b",
        "padding": {"left": 70, "top": 70, "right": 70, "bottom": 70},
        "title": title
    }

    visual = alt.Chart(df).mark_circle().encode(
        x=alt.X(x, title=x),
        y=alt.Y(y, title=y),
        color = alt.Color(target, title=target),
        tooltip=[x,y, target]
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
        stroke='#888',
    ).configure_axisLeft(
        domainColor='#888',
        domainWidth=1
    ).configure_axisTop(
        domainColor='#888',
    )

    return visual

