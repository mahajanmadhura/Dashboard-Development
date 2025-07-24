from app_instance import app
from dashboard_layout import dashboard_layout
import dashboard_callbacks  # Registers callbacks

app.layout = dashboard_layout

if __name__ == "__main__":
    app.run(debug=True)
