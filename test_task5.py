# import pytest
# import dash
# from dash import dcc, html
# from dash.testing.application_runners import import_app


# @pytest.fixture
# def app():
#     return import_app('task4')

# def test_header_present(app):
#     header=app.find_element('h1')
#     assert header is not None, "Header not found in the layout"

# def test_graph_present(app):
#     graph=app.find_element('#sales-graph')
#     assert graph is not None, "Graph not found in the layout"

# def test_radio_items_present(app):
#     regionwise_graph=app.find_element('#regionwise-graph')
#     assert regionwise_graph is not None, "RadioItems not found in the layout"


# def test_graph_update_on_region_change(app):
#     """Test that the graph updates when a region is selected."""
#     regionwise_graph = app.find_element('#regionwise-graph')
#     regionwise_graph.click()  # Click the first option (North)

#     # Check if the graph's figure has updated (you might want to check for specific data in the figure)
#     graph = app.find_element('#sales-graph')
#     assert graph is not None, "Graph not updated after selecting region"



# This file tests parts of your Dash app from task4.py

import pytest
from dash import html, dcc
from task4 import app  # This loads your Dash app

# Test 1: Check if the H1 heading is there
def test_header_is_present():
    layout = app.layout  # Get the layout of the app
    # Go through each item in the layout and find if it's an H1 tag
    for item in layout.children:
        if isinstance(item, html.H1):
            # Check if the text says "Sales Data Visualization"
            assert item.children == "Sales Data Visualization"
            return
    assert False, "H1 heading not found"

# Test 2: Check if the RadioItems (region picker) is there
def test_region_picker_is_present():
    layout = app.layout
    for item in layout.children:
        if isinstance(item, dcc.RadioItems):
            return  # Found it, so we can pass the test
    assert False, "RadioItems (region picker) not found"

# Test 3: Check if the sales graph is there
def test_graph_is_present():
    layout = app.layout
    for item in layout.children:
        if isinstance(item, dcc.Graph):
            # Check if the ID of the graph is 'sales-graph'
            assert item.id == 'sales-graph'
            return
    assert False, "Graph with id 'sales-graph' not found"
