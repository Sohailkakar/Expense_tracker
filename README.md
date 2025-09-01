# Expense_tracker
# Streamlit Expense Tracker

A simple yet powerful expense tracking application built with Streamlit that helps you monitor and visualize your personal expenses.

## Features

- **Add Expenses**: Simple form interface to record new expenses with description, amount, category, and date
- **Data Persistence**: Automatically saves all expenses to a CSV file for data persistence
- **Interactive Filtering**: Filter expenses by category and minimum amount using the sidebar
- **Visual Analytics**: Dynamic pie chart showing expense distribution by category
- **Real-time Summary**: Display total expenses based on current filters
- **Responsive Design**: Clean, professional interface optimized for desktop and mobile

## Screenshots

*Add screenshots of your application here*

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

2. Install required dependencies:
```bash
pip install streamlit pandas plotly
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. Start tracking your expenses:
   - Use the form to add new expenses
   - Apply filters in the sidebar to view specific categories or amounts
   - View your expense distribution in the interactive pie chart

## Project Structure

```
expense-tracker/
│
├── app.py              # Main Streamlit application
├── expenses.csv        # Generated CSV file for data storage
├── requirements.txt    # Python dependencies (optional)
└── README.md          # Project documentation
```

## Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive data visualization

## Data Storage

The application uses a local CSV file (`expenses.csv`) to store expense data. The file is automatically created when you add your first expense and is updated each time you add a new entry.

### CSV Structure
| Column | Description |
|--------|-------------|
| Description | Brief description of the expense |
| Amount | Expense amount in dollars |
| Category | Expense category (Food, Travel, Shopping, Bills, Other) |
| Date | Date of the expense |

## Features in Detail

### Expense Categories
- **Food**: Restaurant meals, groceries, snacks
- **Travel**: Transportation, accommodation, travel expenses
- **Shopping**: Clothing, electronics, personal items
- **Bills**: Utilities, subscriptions, recurring payments
- **Other**: Miscellaneous expenses

### Filtering Options
- **Category Filter**: Select multiple categories to display
- **Amount Filter**: Set minimum expense amount threshold

## Future Enhancements

- [ ] Export data to different formats (Excel, PDF)
- [ ] Monthly/yearly expense reports
- [ ] Budget setting and tracking
- [ ] Expense trends over time
- [ ] Receipt photo upload
- [ ] Multi-currency support
- [ ] Data backup and restore

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request



## Support

If you encounter any issues or have suggestions for improvements, please:
- Open an issue on GitHub


## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Data visualization powered by [Plotly](https://plotly.com/)
- Data handling with [Pandas](https://pandas.pydata.org/)

---

**Start tracking your expenses today and take control of your finances!** 💰📊
