import numpy as np
import pandas as pd

def generate_data(size: int = 100):
    rng = np.random.default_rng()
    return pd.DataFrame({
        "A": rng.normal(size=size),
        "B": rng.normal(size=size),
        "C": rng.normal(size=size)
    })

import panel as pn
import holoviews as hv
pn.extension(sizing_mode='stretch_width')

def plot_curve(df):
    b_plot = hv.Scatter(
        data=df,
        kdims=[('A', 'A-data')],
        vdims=[('B', 'B-data'), ('C', 'C-data')],
        label="B-Data"
        ).opts(
            responsive=True,
            min_height=400,
            tools=["hover"],
            ylabel="Value"
            )
    c_plot = hv.Scatter(
        data=df,
        kdims=[('A', 'A-data')],
        vdims=[('C', 'C-data')],
        label="C-Data"
        )
    return b_plot * c_plot

dashboard = pn.template.BootstrapTemplate(title="SET DASHBOARD TITLE")
dashboard.sidebar.append(pn.Card(pn.pane.Markdown("No site selected"), title="Site Information", collapsible=False))
dashboard.sidebar.append(pn.Card(pn.pane.Markdown("No site selected"), title="Median Event Statistics (95% CI)", collapsible=False))

tabs = pn.Tabs(height=500)
tabs.append(("Controls", pn.pane.Markdown("No data")))
tabs.append(("Curve", pn.pane.Markdown("No data")))
tabs.append(("Distributions", pn.pane.Markdown("No site selected")))
tab_card = pn.Card(tabs, collapsible=False, hide_header=True)
dashboard.main.append(tab_card)

def update_interface(event):
    df = generate_data()
    tabs[1] = ("Curve", plot_curve(df))

button = pn.widgets.Button(name='Click me', button_type='primary')
button.on_click(update_interface)
tabs[0] = button

dashboard.servable()
