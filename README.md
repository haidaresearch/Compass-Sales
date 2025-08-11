# Compass-Sales
Footwear retail sales dashboard, report, and forecast using Excel.

## Business Understanding
• Footwear brand, founded in 1998 in Bandung, Indonesia.  
• Implements a multichannel retailing strategy.  
• Known for the exclusivity of its products on the market.

## Business Questions
• What shoe collection was the most purchased in 2024?  
• During 2024, which store contributed the most revenue?  
• What is the revenue forecast for the next 3 years?

## Excel Function & Feature
SUM, XLOOKUP, FORECAST.ETS, PivotTable, PivotChart.

## Data Schema
For small and medium enterprises, the most suitable data schema type is Star Schema.

![Group 5](https://github.com/user-attachments/assets/b4a44065-b1ec-45bd-b05a-0846b6d4b734)

## Data Source
Dummy data using Python libraries: Pandas, Faker, Random, and Datetime.

## Data Mart
<table>
<tr><th>Central Table</th><th>Look-Up Tables</th></tr>
<tr><td rowspan="5">Sales</td><td>Date</td></tr>
<tr><td>Customer</td></tr>
<tr><td>Product</td></tr>
<tr><td>Store</td></tr>
<tr><td>Payment Method</td></tr>
</table>
Contains 15,000 transactions over 5 years, with 500 customers, 54 products, 5 stores, and 5 payment methods.

## Data Visualization

![Compass Excel Dashboard](https://github.com/user-attachments/assets/319ed72c-39c8-4fd2-ba94-385e93e65ecc)

![Compass Col    Sto](https://github.com/user-attachments/assets/cbb97b3d-45f4-4b80-8cb9-a5e364611c91)

![Compass Sales Forecast](https://github.com/user-attachments/assets/0e3c2296-e8aa-45e9-bb23-1aa98f51c386)

### Visual Principles
• Understand the context → choose an appropriate visual display → eliminate clutter.  
• Form (visualization) follows function (data).  
• Preattentive attributes: size, color, and position on page. Function: to create a visual hierarchy and draw the audience's focus.  
• Lines: show data over time. Bars: plotting categorical data.  
• Leverage alignment of elements and maintain white space to help make the interpretation of visuals a more comfortable experience for the audience.  
• Highlight the important stuff, eliminate distractions, and create a clear visual hierarchy.  
• Clarity over complexity, function over fanciness.

## Insights
• In 2024, the most purchased collection was Gazelle (1,240 units).  
• The store that contributed the most revenue during 2024 was the website, accounting for 21.28%.  
• In the next three years, revenue is predicted to gradually decline.

## Recommendations
• Launch new products in the Gazelle collection to maintain product momentum.  
• Check whether the marketplace, social commerce, and offline retail have been maximized or not.  
• Try dynamic pricing and loyalty discounts for repeat buyers.
