import plotly.graph_objs as go
import numpy as np

# ��������� ����� ������� ����� ������ ��� ���������
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))  # ���������� ������ ������� ��� ������������

# �������� 3D surface plot
surface = go.Surface(
    x=x, y=y, z=z,
    colorscale='Viridis'   # �������� �������
)

# ��������� ������
layout = go.Layout(
    scene=dict(
        xaxis_title='X AXIS',
        yaxis_title='Y AXIS',
        zaxis_title='Z AXIS'
    ),
    title='3D Surface Plot - Detailed Landscape'
)

# �������� ������
fig = go.Figure(data=[surface], layout=layout)

# ���������� ������ � HTML ���� � �������� � ��������
fig.write_html("3d_detailed_surface_plot.html", auto_open=True)
