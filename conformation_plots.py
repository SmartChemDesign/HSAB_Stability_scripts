from plotly import express as px
import pandas as pd
from shap.plots import waterfall
palette = px.colors.qualitative.D3
plotter_dict = [["eg", "sf", "Hardness, eV", "Separation factor", [1, 10, 100, 1000, 10000, 100000]],
                #["eg", "D(Am)", "Hardness, eV", "D(Am)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
                #["eg", "D(Eu)", "Hardness, eV", "D(Eu)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],

                #["conf_std", "sf", "Conformation mobility, Eh", "Separation factor", [1, 10, 100, 1000, 10000, 100000]],
                #["conf_std", "D(Am)", "Conformation mobility, Eh", "D(Am)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
                #["conf_std", "D(Eu)", "Conformation mobility, Eh", "D(Eu)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],

                ["esp", "sf", "Electrostatic potential, V", "Separation factor", [1, 10, 100, 1000, 10000, 100000]],
                #["esp", "D(Am)", "Electrostatic potential, eV", "D(Am)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
                #["esp", "D(Eu)", "Electrostatic potential, eV", "D(Eu)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],

                # ["pKa", "sf", "pKa", "Separation factor", [1, 10, 100, 1000, 10000, 100000]],
                # ["pKa", "D(Am)", "pKa", "D(Am)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
                # ["pKa", "D(Eu)", "pKa", "D(Eu)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],

                # ["Solven_Epsilon", "sf", "Dielectric Constant", "Separation factor", [1, 10, 100, 1000, 10000, 100000]],
                # ["Solven_Epsilon", "D(Am)", "Dielectric Constant", "D(Am)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
                # ["Solven_Epsilon", "D(Eu)", "Dielectric Constant", "D(Eu)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],

                # ["Surface_tension", "sf", "Solvent surface tension", "Separation factor", [1, 10, 100, 1000, 10000, 100000]],
                # ["Surface_tension", "D(Am)", "Solvent surface tension", "D(Am)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
                # ["Surface_tension", "D(Eu)", "Solvent surface tension", "D(Eu)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],

                ["preorg_energy", "sf", "Preorganization energy, eV", "Separation factor", [1, 10, 100, 1000, 10000, 100000]],
                # ["preorg_energy", "D(Am)", "Preorganization energy", "D(Am)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
                # ["preorg_energy", "D(Eu)", "Preorganization energy", "D(Eu)", [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
                ]

df = pd.read_csv("/home/cairne/WorkProjects/logK_hardness_paper/plots/final_res_diff_fixed.csv"#, delimiter=";"
                 )
df["preorg_energy"] = [-i * 27.2114 for i in df["preorg_energy"]]
df["eg"] = [-i for i in df["eg"]]

print(px.colors.qualitative.G10)
for x_value, y_value, x_title, y_title, y_axis in plotter_dict:
    fig = px.scatter(df, x=x_value, y=y_value, log_y=True, template="plotly_white", symbol="paper_short",
                     color="paper_short",
                     color_discrete_sequence=px.colors.qualitative.Bold[:-1] + [px.colors.qualitative.Plotly[2]]# + [px.colors.qualitative.G10[:-1]]
                     )

    fig.update_xaxes(mirror=True, ticks='outside', showline=True)
    fig.update_yaxes(mirror=True, ticks='outside', showline=True)
    fig.update_traces(marker={'size': 12})
    fig.update_layout(
        yaxis_title=y_title,
        xaxis_title=x_title,
        font=dict(
            size=20,
        )
    )

    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0,
        font=dict(
            size=18,
        ),
        title=None
    ))
    fig.update_xaxes(mirror=True, ticks='outside', showline=True)
    fig.update_yaxes(mirror=True, ticks='outside', showline=True)
    fig.update_xaxes(showline=True, linewidth=0.5, linecolor='black', gridwidth=0.1, gridcolor='gray', zeroline=True,
                     zerolinewidth=0.1, zerolinecolor='black')

    fig.update_yaxes(showline=True, linewidth=0.5, linecolor='black', gridwidth=0.1, gridcolor='gray', zeroline=True,
                     zerolinewidth=0.1, zerolinecolor='black')
    fig.update_yaxes(type="log", tickvals=y_axis)
    fig.update_layout(showlegend=False)
    fig.write_image(f"{y_value}_{x_value}_final.png", width=800, height=600)
