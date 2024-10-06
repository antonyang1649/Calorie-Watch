from flask import Flask, render_template, request


app = Flask(__name__)


#Food data
foods = [
    {'name': 'Acorn Squash', 'calories': 40},
    {'name': 'Adzuki Beans', 'calories': 128},
    {'name': 'Alfalfa Sprouts', 'calories': 23},
    {'name': 'Almond Milk (unsweetened)', 'calories': 30},
    {'name': 'Almonds', 'calories': 575},
    {'name': 'Anchovy', 'calories': 131},
    {'name': 'Angus Bacon & Cheese', 'calories': 790},
    {'name': 'Angus Deluxe', 'calories': 770},
    {'name': 'Anise', 'calories': 337},
    {'name': 'Apple Juice', 'calories': 46},
    {'name': 'Apple Pie', 'calories': 237},
    {'name': 'Apple Slices', 'calories': 15},
    {'name': 'Apple', 'calories': 52},
    {'name': 'Apricot', 'calories': 48},
    {'name': 'Artichoke', 'calories': 47},
    {'name': 'Arugula', 'calories': 25},
    {'name': 'Asparagus', 'calories': 20},
    {'name': 'Avocado Oil', 'calories': 884},
    {'name': 'Avocado', 'calories': 160},
    {'name': 'Bacon Cheddar McChicken', 'calories': 480},
    {'name': 'Bacon Cheeseburger', 'calories': 360},
    {'name': 'Bacon Clubhouse Burger', 'calories': 720},
    {'name': 'Bacon McDouble', 'calories': 460},
    {'name': 'Bacon Ranch Grilled Chicken Salad', 'calories': 320},
    {'name': 'Bacon, Egg & Cheese Bagel with Egg Whites', 'calories': 570},
    {'name': 'Bacon, Egg & Cheese Bagel', 'calories': 620},
    {'name': 'Bacon, Egg & Cheese Biscuit', 'calories': 450},
    {'name': 'Bacon, Egg & Cheese McGriddles', 'calories': 420},
    {'name': 'Bacon', 'calories': 541},
    {'name': 'Bagel', 'calories': 257},
    {'name': 'Baguette', 'calories': 248},
    {'name': 'Baked Potato', 'calories': 93},
    {'name': 'Baklava', 'calories': 428},
    {'name': 'Bamboo Shoots', 'calories': 11},
    {'name': 'Banana Squash', 'calories': 31},
    {'name': 'Banana', 'calories': 89},
    {'name': 'Barley', 'calories': 354},
    {'name': 'Basil', 'calories': 22},
    {'name': 'Bass', 'calories': 124},
    {'name': 'Bay Leaves', 'calories': 313},
    {'name': 'BBQ Wings', 'calories': 285},
    {'name': 'Bean Sprouts', 'calories': 31},
    {'name': 'Beef and Broccoli', 'calories': 232},
    {'name': 'Beef Back Ribs', 'calories': 280},
    {'name': 'Beef Bone Marrow', 'calories': 770},
    {'name': 'Beef Bottom Round', 'calories': 210},
    {'name': 'Beef Brains', 'calories': 143},
    {'name': 'Beef Brisket', 'calories': 246},
    {'name': 'Beef Burrito', 'calories': 550},
    {'name': 'Beef Cheek', 'calories': 150},
    {'name': 'Beef Chimichanga', 'calories': 483},
    {'name': 'Beef Chuck Roast', 'calories': 230},
    {'name': 'Beef Chuck', 'calories': 250},
    {'name': 'Beef Clod', 'calories': 200},
    {'name': 'Beef Drippings', 'calories': 884},
    {'name': 'Beef Empanada', 'calories': 267},
    {'name': 'Beef Enchiladas', 'calories': 400},
    {'name': 'Beef Eye Round', 'calories': 210},
    {'name': 'Beef Eyes', 'calories': 50},
    {'name': 'Beef Fajitas', 'calories': 400},
    {'name': 'Beef Fat', 'calories': 884},
    {'name': 'Beef Flank Steak', 'calories': 204},
    {'name': 'Beef Grease', 'calories': 884},
    {'name': 'Beef Heart', 'calories': 112},
    {'name': 'Beef Heel', 'calories': 210},
    {'name': 'Beef Hock', 'calories': 170},
    {'name': 'Beef Jerky', 'calories': 410},
    {'name': 'Beef Kabobs', 'calories': 200},
    {'name': 'Beef Kidney', 'calories': 112},
    {'name': 'Beef Knuckle', 'calories': 210},
    {'name': 'Beef Liver', 'calories': 135},
    {'name': 'Beef Marrow', 'calories': 770},
    {'name': 'Beef Nachos', 'calories': 386},
    {'name': 'Beef Neck', 'calories': 200},
    {'name': 'Beef Oil', 'calories': 884},
    {'name': 'Beef Oxtail', 'calories': 262},
    {'name': 'Beef Plate', 'calories': 240},
    {'name': 'Beef Quesadilla', 'calories': 485},
    {'name': 'Beef Ribs', 'calories': 380},
    {'name': 'Beef Roast', 'calories': 255},
    {'name': 'Beef Round Roast', 'calories': 240},
    {'name': 'Beef Round Steak', 'calories': 240},
    {'name': 'Beef Round Tip', 'calories': 210},
    {'name': 'Beef Round', 'calories': 210},
    {'name': 'Beef Rump Cap', 'calories': 240},
    {'name': 'Beef Rump Roast', 'calories': 240},
    {'name': 'Beef Rump Steak', 'calories': 240},
    {'name': 'Beef Rump Tail', 'calories': 240},
    {'name': 'Beef Rump', 'calories': 210},
    {'name': 'Beef Shank', 'calories': 178},
    {'name': 'Beef Shin', 'calories': 170},
    {'name': 'Beef Short Ribs', 'calories': 260},
    {'name': 'Beef Shortening', 'calories': 884},
    {'name': 'Beef Shoulder', 'calories': 250},
    {'name': 'Beef Silverside', 'calories': 220},
    {'name': 'Beef Sirloin', 'calories': 218},
    {'name': 'Beef Skirt Steak', 'calories': 227},
    {'name': 'Beef Stew', 'calories': 118},
    {'name': 'Beef Stroganoff', 'calories': 258},
    {'name': 'Beef Suet', 'calories': 884},
    {'name': 'Beef Tacos', 'calories': 226},
    {'name': 'Beef Tail', 'calories': 250},
    {'name': 'Beef Tallow', 'calories': 902},
    {'name': 'Beef Tenderloin', 'calories': 194},
    {'name': 'Beef Tendon', 'calories': 150},
    {'name': 'Beef Tongue', 'calories': 220},
    {'name': 'Beef Top Round', 'calories': 210},
    {'name': 'Beef Topside', 'calories': 210},
    {'name': 'Beef Tostada', 'calories': 278},
    {'name': 'Beef Tri-Tip', 'calories': 245},
    {'name': 'Beef Trimmings', 'calories': 510},
    {'name': 'Beef Tripe', 'calories': 85},
    {'name': 'Beef Wellington', 'calories': 360},
    {'name': 'Beer', 'calories': 154},
    {'name': 'Beet Greens', 'calories': 22},
    {'name': 'Beetroot', 'calories': 43},
    {'name': 'Bell Pepper', 'calories': 31},
    {'name': 'Bibb Lettuce', 'calories': 13},
    {'name': 'Big Breakfast with Hotcakes', 'calories': 1350},
    {'name': 'Big Breakfast', 'calories': 750},
    {'name': 'Big Chicken Fillet Sandwich', 'calories': 520},
    {'name': 'Big Mac', 'calories': 550},
    {'name': 'Biryani', 'calories': 290},
    {'name': 'Biscuit', 'calories': 190},
    {'name': 'Biscuit', 'calories': 460},
    {'name': 'Black Beans', 'calories': 132},
    {'name': 'Black Tea', 'calories': 2},
    {'name': 'Black-Eyed Peas', 'calories': 114},
    {'name': 'Blackberry', 'calories': 43},
    {'name': 'BLT Sandwich', 'calories': 298},
    {'name': 'Blueberry Muffin', 'calories': 370},
    {'name': 'Blueberry', 'calories': 57},
    {'name': 'Bok Choy', 'calories': 13},
    {'name': 'Bologna', 'calories': 305},
    {'name': 'Brazil Nuts', 'calories': 659},
    {'name': 'Breadstick', 'calories': 366},
    {'name': 'Brie Cheese', 'calories': 334},
    {'name': 'Brioche', 'calories': 313},
    {'name': 'Broccoli Sprouts', 'calories': 35},
    {'name': 'Broccoli', 'calories': 34},
    {'name': 'Brown Rice', 'calories': 111},
    {'name': 'Brownie', 'calories': 466},
    {'name': 'Brussels Sprouts', 'calories': 43},
    {'name': 'Buffalo Wings', 'calories': 246},
    {'name': 'Burdock Root', 'calories': 72},
    {'name': 'Burrito', 'calories': 290},
    {'name': 'Butter Beans', 'calories': 113},
    {'name': 'Butter', 'calories': 70},
    {'name': 'Butterhead Lettuce', 'calories': 13},
    {'name': 'Buttermilk', 'calories': 52},
    {'name': 'Butternut Squash', 'calories': 45},
    {'name': 'Cabbage', 'calories': 25},
    {'name': 'Caesar Salad', 'calories': 190},
    {'name': 'California Roll', 'calories': 255},
    {'name': 'Canned Salmon', 'calories': 162},
    {'name': 'Canned Tuna', 'calories': 128},
    {'name': 'Cannellini Beans', 'calories': 119},
    {'name': 'Cannoli', 'calories': 334},
    {'name': 'Cantaloupe', 'calories': 34},
    {'name': 'Cappuccino', 'calories': 120},
    {'name': 'Caramel Frappe (Small)', 'calories': 450},
    {'name': 'Caramel Sundae', 'calories': 330},
    {'name': 'Caraway', 'calories': 333},
    {'name': 'Cardamom', 'calories': 311},
    {'name': 'Carrot', 'calories': 41},
    {'name': 'Cashews', 'calories': 553},
    {'name': 'Cassava', 'calories': 160},
    {'name': 'Catfish', 'calories': 105},
    {'name': 'Cauliflower', 'calories': 25},
    {'name': 'Celeriac', 'calories': 42},
    {'name': 'Celery', 'calories': 16},
    {'name': 'Challah', 'calories': 298},
    {'name': 'Chanterelle Mushroom', 'calories': 38},
    {'name': 'Chard', 'calories': 19},
    {'name': 'Chayote Squash', 'calories': 19},
    {'name': 'Cheddar Cheese', 'calories': 403},
    {'name': 'Cheese Crackers', 'calories': 540},
    {'name': 'Cheese Puffs', 'calories': 497},
    {'name': 'Cheeseburger Deluxe', 'calories': 280},
    {'name': 'Cheeseburger', 'calories': 300},
    {'name': 'Cheesecake', 'calories': 321},
    {'name': 'Cherry', 'calories': 50},
    {'name': 'Chia Seeds', 'calories': 486},
    {'name': 'Chicken Breast', 'calories': 165},
    {'name': 'Chicken Burrito', 'calories': 500},
    {'name': 'Chicken Caesar Salad', 'calories': 220},
    {'name': 'Chicken Chimichanga', 'calories': 443},
    {'name': 'Chicken Drumstick', 'calories': 216},
    {'name': 'Chicken Enchiladas', 'calories': 360},
    {'name': 'Chicken Fajitas', 'calories': 350},
    {'name': 'Chicken McNuggets (10 pieces)', 'calories': 470},
    {'name': 'Chicken McNuggets (20 pieces)', 'calories': 940},
    {'name': 'Chicken McNuggets (6 pieces)', 'calories': 280},
    {'name': 'Chicken Nachos', 'calories': 346},
    {'name': 'Chicken Nugget', 'calories': 287},
    {'name': 'Chicken Quesadilla', 'calories': 475},
    {'name': 'Chicken Ranch BLT Sandwich', 'calories': 610},
    {'name': 'Chicken Salad', 'calories': 200},
    {'name': 'Chicken Sandwich', 'calories': 340},
    {'name': 'Chicken Tacos', 'calories': 231},
    {'name': 'Chicken Tenders', 'calories': 270},
    {'name': 'Chicken Thigh', 'calories': 209},
    {'name': 'Chicken Wing', 'calories': 203},
    {'name': 'Chickpeas', 'calories': 164},
    {'name': 'Chicory', 'calories': 23},
    {'name': 'Chili Pepper', 'calories': 40},
    {'name': 'Chimichanga', 'calories': 443},
    {'name': 'Chipotle BBQ Sauce', 'calories': 60},
    {'name': 'Chives', 'calories': 30},
    {'name': 'Chocolate Cake', 'calories': 352},
    {'name': 'Chocolate Chip Cookie', 'calories': 160},
    {'name': 'Chocolate Shake (Small)', 'calories': 530},
    {'name': 'Chorizo', 'calories': 455},
    {'name': 'Chow Mein', 'calories': 510},
    {'name': 'Churros', 'calories': 325},
    {'name': 'Ciabatta', 'calories': 271},
    {'name': 'Cilantro Seeds', 'calories': 298},
    {'name': 'Cilantro', 'calories': 23},
    {'name': 'Cinnamon Melts', 'calories': 460},
    {'name': 'Cinnamon', 'calories': 247},
    {'name': 'Clam', 'calories': 74},
    {'name': 'Clementine', 'calories': 35},
    {'name': 'Clove', 'calories': 274},
    {'name': 'Cobb Salad', 'calories': 160},
    {'name': 'Coconut Milk', 'calories': 230},
    {'name': 'Coconut Water', 'calories': 19},
    {'name': 'Coconut', 'calories': 354},
    {'name': 'Cod', 'calories': 82},
    {'name': 'Coffee', 'calories': 2},
    {'name': 'Cola', 'calories': 150},
    {'name': 'Coleslaw', 'calories': 152},
    {'name': 'Collard Greens', 'calories': 32},
    {'name': 'Cookie', 'calories': 200},
    {'name': 'Coriander', 'calories': 298},
    {'name': 'Corn Dog', 'calories': 225},
    {'name': 'Corn Tortilla', 'calories': 218},
    {'name': 'Corn', 'calories': 96},
    {'name': 'Cornbread', 'calories': 330},
    {'name': 'Corned Beef', 'calories': 250},
    {'name': 'Cottage Cheese', 'calories': 98},
    {'name': 'Couscous Salad', 'calories': 121},
    {'name': 'Couscous', 'calories': 112},
    {'name': 'Crab', 'calories': 97},
    {'name': 'Cracker', 'calories': 502},
    {'name': 'Cranberry Juice', 'calories': 46},
    {'name': 'Cranberry', 'calories': 46},
    {'name': 'Cream Cheese', 'calories': 342},
    {'name': 'Creamy Caesar Sauce', 'calories': 130},
    {'name': 'Creamy Ranch Sauce', 'calories': 200},
    {'name': 'Croissant', 'calories': 406},
    {'name': 'Crookneck Squash', 'calories': 19},
    {'name': 'Croutons', 'calories': 407},
    {'name': 'Cucumber', 'calories': 16},
    {'name': 'Cumin', 'calories': 375},
    {'name': 'Cupcake', 'calories': 292},
    {'name': 'Curry Leaves', 'calories': 108},
    {'name': 'Curry', 'calories': 250},
    {'name': 'Daikon', 'calories': 18},
    {'name': 'Dal', 'calories': 200},
    {'name': 'Dandelion Greens', 'calories': 45},
    {'name': 'Delicata Squash', 'calories': 34},
    {'name': 'Diet Soda', 'calories': 0},
    {'name': 'Dill Seeds', 'calories': 305},
    {'name': 'Dill', 'calories': 43},
    {'name': 'Donut', 'calories': 452},
    {'name': 'Dosa', 'calories': 133},
    {'name': 'Double Bacon Cheeseburger', 'calories': 560},
    {'name': 'Double Bacon Clubhouse Burger', 'calories': 930},
    {'name': 'Double Big Chicken Fillet Sandwich', 'calories': 830},
    {'name': 'Double Big Mac', 'calories': 720},
    {'name': 'Double Cheeseburger', 'calories': 450},
    {'name': 'Double Filet-O-Fish', 'calories': 660},
    {'name': 'Double McChicken', 'calories': 580},
    {'name': 'Double McDouble', 'calories': 570},
    {'name': 'Double McRib', 'calories': 730},
    {'name': 'Double Quarter Pounder with Cheese', 'calories': 740},
    {'name': 'Dragon Fruit', 'calories': 50},
    {'name': 'Duck Breast', 'calories': 337},
    {'name': 'Duck Leg', 'calories': 340},
    {'name': 'Dumpling', 'calories': 41},
    {'name': 'Edamame', 'calories': 121},
    {'name': 'Egg McMuffin', 'calories': 300},
    {'name': 'Egg Roll', 'calories': 180},
    {'name': 'Egg White Delight McMuffin', 'calories': 250},
    {'name': 'Egg White', 'calories': 52},
    {'name': 'Egg Yolk', 'calories': 322},
    {'name': 'Egg', 'calories': 155},
    {'name': 'Eggnog', 'calories': 223},
    {'name': 'Eggplant', 'calories': 25},
    {'name': 'Enchilada', 'calories': 168},
    {'name': 'Endive', 'calories': 17},
    {'name': 'Energy Bar', 'calories': 250},
    {'name': 'Energy Drink', 'calories': 45},
    {'name': 'English Muffin', 'calories': 223},
    {'name': 'Enoki Mushroom', 'calories': 37},
    {'name': 'Epazote', 'calories': 32},
    {'name': 'Escarole', 'calories': 15},
    {'name': 'Espresso', 'calories': 1},
    {'name': 'Fajita', 'calories': 320},
    {'name': 'Fava Beans', 'calories': 88},
    {'name': 'Fennel Seeds', 'calories': 345},
    {'name': 'Fennel', 'calories': 31},
    {'name': 'Fenugreek Leaves', 'calories': 49},
    {'name': 'Fenugreek', 'calories': 323},
    {'name': 'Feta Cheese', 'calories': 264},
    {'name': 'Fiddlehead Ferns', 'calories': 34},
    {'name': 'Fig', 'calories': 74},
    {'name': 'Filet-O-Fish Sandwich', 'calories': 380},
    {'name': 'Fish Filet Patty', 'calories': 300},
    {'name': 'Fish Sandwich', 'calories': 390},
    {'name': 'Fish Stick', 'calories': 264},
    {'name': 'Flan', 'calories': 146},
    {'name': 'Flax Seeds', 'calories': 534},
    {'name': 'Flaxseed Oil', 'calories': 884},
    {'name': 'Flounder', 'calories': 86},
    {'name': 'Flour Tortilla', 'calories': 333},
    {'name': 'Focaccia', 'calories': 292},
    {'name': 'French Fries (Large)', 'calories': 510},
    {'name': 'French Fries (Medium)', 'calories': 340},
    {'name': 'French Fries (Small)', 'calories': 230},
    {'name': 'Fried Rice', 'calories': 163},
    {'name': 'Frisee', 'calories': 17},
    {'name': 'Fruit \'n Yogurt Parfait', 'calories': 150},
    {'name': 'Fruit & Maple Oatmeal', 'calories': 290},
    {'name': 'Fruit and Maple Oatmeal', 'calories': 290},
    {'name': 'Fruit and Yogurt Parfait', 'calories': 150},
    {'name': 'Fruit Salad', 'calories': 50},
    {'name': 'Fruit Snacks', 'calories': 350},
    {'name': 'Galangal', 'calories': 71},
    {'name': 'Garlic Bread', 'calories': 350},
    {'name': 'Garlic', 'calories': 149},
    {'name': 'Gelato', 'calories': 208},
    {'name': 'General Tso\'s Chicken', 'calories': 295},
    {'name': 'Ginger Ale', 'calories': 124},
    {'name': 'Ginger', 'calories': 80},
    {'name': 'Gnocchi', 'calories': 175},
    {'name': 'Goat Cheese', 'calories': 364},
    {'name': 'Goose', 'calories': 305},
    {'name': 'Graham Cracker', 'calories': 431},
    {'name': 'Granola Bar', 'calories': 193},
    {'name': 'Granola', 'calories': 471},
    {'name': 'Grape Juice', 'calories': 60},
    {'name': 'Grapes', 'calories': 69},
    {'name': 'Grapeseed Oil', 'calories': 884},
    {'name': 'Great Northern Beans', 'calories': 118},
    {'name': 'Greek Salad', 'calories': 95},
    {'name': 'Greek Yogurt', 'calories': 59},
    {'name': 'Green Beans', 'calories': 31},
    {'name': 'Green Leaf Lettuce', 'calories': 15},
    {'name': 'Green Lentils', 'calories': 116},
    {'name': 'Green Onion', 'calories': 32},
    {'name': 'Green Tea', 'calories': 0},
    {'name': 'Grilled Cheese', 'calories': 378},
    {'name': 'Grilled Chicken Salad', 'calories': 190},
    {'name': 'Grilled Chicken Sandwich', 'calories': 350},
    {'name': 'Ground Beef', 'calories': 250},
    {'name': 'Ground Lamb', 'calories': 283},
    {'name': 'Ground Turkey', 'calories': 187},
    {'name': 'Guava', 'calories': 68},
    {'name': 'Gulab Jamun', 'calories': 143},
    {'name': 'Habanero', 'calories': 40},
    {'name': 'Haddock', 'calories': 90},
    {'name': 'Halibut', 'calories': 111},
    {'name': 'Ham Sandwich', 'calories': 220},
    {'name': 'Ham', 'calories': 145},
    {'name': 'Hamburger Bun', 'calories': 264},
    {'name': 'Hamburger', 'calories': 250},
    {'name': 'Hash Browns', 'calories': 150},
    {'name': 'Hazelnuts', 'calories': 628},
    {'name': 'Heavy Cream', 'calories': 345},
    {'name': 'Hempseed Oil', 'calories': 884},
    {'name': 'Herbal Tea', 'calories': 2},
    {'name': 'Herring', 'calories': 158},
    {'name': 'Honey Mustard Sauce', 'calories': 60},
    {'name': 'Honeydew', 'calories': 36},
    {'name': 'Horse Radish', 'calories': 48},
    {'name': 'Hot Chocolate', 'calories': 192},
    {'name': 'Hot Dog Bun', 'calories': 138},
    {'name': 'Hot Dog', 'calories': 151},
    {'name': 'Hot Fudge Sundae', 'calories': 330},
    {'name': 'Hot Mustard Sauce', 'calories': 60},
    {'name': 'Hotcake Syrup', 'calories': 130},
    {'name': 'Hotcakes (without syrup and butter)', 'calories': 600},
    {'name': 'Hotcakes and Sausage', 'calories': 780},
    {'name': 'Hotcakes', 'calories': 600},
    {'name': 'Houttuynia', 'calories': 21},
    {'name': 'Hubbard Squash', 'calories': 40},
    {'name': 'Ice Cream', 'calories': 207},
    {'name': 'Iceberg Lettuce', 'calories': 14},
    {'name': 'Iced Caramel Mocha (Small)', 'calories': 280},
    {'name': 'Iced Coffee (Small)', 'calories': 140},
    {'name': 'Iced Latte (Small)', 'calories': 120},
    {'name': 'Iced Mocha (Small)', 'calories': 250},
    {'name': 'Iced Tea', 'calories': 30},
    {'name': 'Jalapeno', 'calories': 29},
    {'name': 'Jelly', 'calories': 50},
    {'name': 'Jicama', 'calories': 38},
    {'name': 'Kabocha Squash', 'calories': 49},
    {'name': 'Kaffir Lime Leaves', 'calories': 44},
    {'name': 'Kaiser Roll', 'calories': 250},
    {'name': 'Kale', 'calories': 49},
    {'name': 'Karela', 'calories': 17},
    {'name': 'Kidney Beans', 'calories': 127},
    {'name': 'Kiwi', 'calories': 61},
    {'name': 'Kohlrabi Greens', 'calories': 27},
    {'name': 'Kohlrabi', 'calories': 27},
    {'name': 'Kung Pao Chicken', 'calories': 290},
    {'name': 'Lamb Chop', 'calories': 282},
    {'name': 'Lamb Shank', 'calories': 231},
    {'name': 'Lambsquarters', 'calories': 43},
    {'name': 'Lasagna', 'calories': 163},
    {'name': 'Latte', 'calories': 190},
    {'name': 'Leek', 'calories': 61},
    {'name': 'Lemon', 'calories': 29},
    {'name': 'Lemonade', 'calories': 99},
    {'name': 'Lentils', 'calories': 116},
    {'name': 'Lettuce', 'calories': 15},
    {'name': 'Lima Beans', 'calories': 113},
    {'name': 'Lime', 'calories': 30},
    {'name': 'Linseed', 'calories': 534},
    {'name': 'Lo Mein', 'calories': 138},
    {'name': 'Loaded Potato', 'calories': 481},
    {'name': 'Lobster', 'calories': 89},
    {'name': 'Lotus Root', 'calories': 74},
    {'name': 'Lovage', 'calories': 44},
    {'name': 'Luffa', 'calories': 20},
    {'name': 'Lychee', 'calories': 66},
    {'name': 'Macadamia Nuts', 'calories': 718},
    {'name': 'Macadamia Oil', 'calories': 884},
    {'name': 'Macaroni', 'calories': 157},
    {'name': 'Mace', 'calories': 475},
    {'name': 'Mache', 'calories': 21},
    {'name': 'Mackerel', 'calories': 205},
    {'name': 'Mango Pineapple Smoothie', 'calories': 220},
    {'name': 'Mango', 'calories': 60},
    {'name': 'Mapo Tofu', 'calories': 234},
    {'name': 'Marjoram', 'calories': 271},
    {'name': 'Mashed Potatoes', 'calories': 88},
    {'name': 'Matzo', 'calories': 333},
    {'name': 'McChicken Sandwich', 'calories': 400},
    {'name': 'McChicken', 'calories': 370},
    {'name': 'McDouble with Bacon', 'calories': 460},
    {'name': 'McDouble', 'calories': 390},
    {'name': 'McFlurry with M&M\'s', 'calories': 530},
    {'name': 'McFlurry with Oreo Cookies', 'calories': 510},
    {'name': 'McGriddles Bacon, Egg & Cheese with Egg Whites', 'calories': 420},
    {'name': 'McGriddles Bacon, Egg & Cheese', 'calories': 460},
    {'name': 'McGriddles Sausage, Egg & Cheese with Egg Whites', 'calories': 500},
    {'name': 'McGriddles Sausage, Egg & Cheese', 'calories': 550},
    {'name': 'McRib Sandwich', 'calories': 500},
    {'name': 'McRib', 'calories': 500},
    {'name': 'Mexican Mint Marigold', 'calories': 295},
    {'name': 'Milk', 'calories': 42},
    {'name': 'Milkshake', 'calories': 378},
    {'name': 'Mint', 'calories': 70},
    {'name': 'Mizuna', 'calories': 22},
    {'name': 'Mocha Frappe (Small)', 'calories': 450},
    {'name': 'Morel Mushroom', 'calories': 31},
    {'name': 'Mozzarella Cheese', 'calories': 280},
    {'name': 'Mozzarella Stick', 'calories': 301},
    {'name': 'Muffin', 'calories': 365},
    {'name': 'Mung Beans', 'calories': 347},
    {'name': 'Mushroom', 'calories': 22},
    {'name': 'Mussel', 'calories': 86},
    {'name': 'Mustard Greens', 'calories': 27},
    {'name': 'Mustard Seeds', 'calories': 508},
    {'name': 'Naan Bread', 'calories': 317},
    {'name': 'Naan', 'calories': 317},
    {'name': 'Nachos', 'calories': 346},
    {'name': 'Navy Beans', 'calories': 140},
    {'name': 'Nectarine', 'calories': 44},
    {'name': 'Nigella', 'calories': 345},
    {'name': 'Nutmeg', 'calories': 525},
    {'name': 'Oat Milk', 'calories': 43},
    {'name': 'Oatmeal', 'calories': 68},
    {'name': 'Octopus', 'calories': 82},
    {'name': 'Okra', 'calories': 33},
    {'name': 'Onion Rings', 'calories': 411},
    {'name': 'Onion', 'calories': 40},
    {'name': 'Opo Squash', 'calories': 12},
    {'name': 'Orange Chicken', 'calories': 260},
    {'name': 'Orange Juice', 'calories': 45},
    {'name': 'Orange', 'calories': 47},
    {'name': 'Oregano', 'calories': 265},
    {'name': 'Oyster Mushroom', 'calories': 33},
    {'name': 'Oyster', 'calories': 81},
    {'name': 'Pad Thai', 'calories': 300},
    {'name': 'Pakora', 'calories': 315},
    {'name': 'Papalo', 'calories': 23},
    {'name': 'Papaya', 'calories': 43},
    {'name': 'Paratha', 'calories': 258},
    {'name': 'Parmesan Cheese', 'calories': 431},
    {'name': 'Parsley', 'calories': 36},
    {'name': 'Parsnip', 'calories': 75},
    {'name': 'Passion Fruit', 'calories': 97},
    {'name': 'Pasta', 'calories': 157},
    {'name': 'Pastrami', 'calories': 151},
    {'name': 'Pattypan Squash', 'calories': 16},
    {'name': 'Peach', 'calories': 39},
    {'name': 'Peanuts', 'calories': 567},
    {'name': 'Peas', 'calories': 81},
    {'name': 'Pecan Pie', 'calories': 503},
    {'name': 'Pecans', 'calories': 691},
    {'name': 'Peking Duck', 'calories': 335},
    {'name': 'Pepperoni', 'calories': 494},
    {'name': 'Perilla Leaves', 'calories': 37},
    {'name': 'Pho', 'calories': 375},
    {'name': 'Pickled Herring', 'calories': 262},
    {'name': 'Pine Nuts', 'calories': 673},
    {'name': 'Pineapple', 'calories': 50},
    {'name': 'Pinto Beans', 'calories': 143},
    {'name': 'Pistachios', 'calories': 562},
    {'name': 'Pita Bread', 'calories': 275},
    {'name': 'Pizza', 'calories': 266},
    {'name': 'Plum', 'calories': 46},
    {'name': 'Pomegranate', 'calories': 83},
    {'name': 'Popcorn', 'calories': 375},
    {'name': 'Poppy Seeds', 'calories': 525},
    {'name': 'Popsicle', 'calories': 50},
    {'name': 'Pork Belly', 'calories': 518},
    {'name': 'Pork Chop', 'calories': 231},
    {'name': 'Pork Loin', 'calories': 242},
    {'name': 'Portobello Mushroom', 'calories': 22},
    {'name': 'Potato Chips', 'calories': 536},
    {'name': 'Potato Salad', 'calories': 143},
    {'name': 'Potato Skins', 'calories': 510},
    {'name': 'Potato', 'calories': 77},
    {'name': 'Premium Crispy Chicken Club Sandwich', 'calories': 670},
    {'name': 'Premium Grilled Chicken Classic Sandwich', 'calories': 510},
    {'name': 'Premium Grilled Chicken Club Sandwich', 'calories': 620},
    {'name': 'Premium McWrap Chicken & Bacon (Crispy)', 'calories': 670},
    {'name': 'Premium McWrap Chicken & Bacon (Grilled)', 'calories': 470},
    {'name': 'Premium McWrap Chicken & Ranch (Crispy)', 'calories': 610},
    {'name': 'Premium McWrap Chicken & Ranch (Grilled)', 'calories': 420},
    {'name': 'Premium McWrap Southwest Chicken (Crispy)', 'calories': 610},
    {'name': 'Premium McWrap Southwest Chicken (Grilled)', 'calories': 420},
    {'name': 'Pretzel', 'calories': 380},
    {'name': 'Pretzels', 'calories': 380},
    {'name': 'Prosciutto', 'calories': 225},
    {'name': 'Protein Bar', 'calories': 225},
    {'name': 'Pumpkin Pie', 'calories': 323},
    {'name': 'Pumpkin Seed Oil', 'calories': 884},
    {'name': 'Pumpkin Seeds', 'calories': 574},
    {'name': 'Pumpkin', 'calories': 26},
    {'name': 'Purslane', 'calories': 16},
    {'name': 'Quail', 'calories': 123},
    {'name': 'Quarter Pounder Bacon', 'calories': 590},
    {'name': 'Quarter Pounder Deluxe', 'calories': 590},
    {'name': 'Quarter Pounder with Cheese', 'calories': 530},
    {'name': 'Quarter Pounder', 'calories': 530},
    {'name': 'Quesadilla', 'calories': 360},
    {'name': 'Quinoa', 'calories': 120},
    {'name': 'Radicchio', 'calories': 23},
    {'name': 'Radish', 'calories': 16},
    {'name': 'Radishes', 'calories': 16},
    {'name': 'Ramen', 'calories': 436},
    {'name': 'Ramps', 'calories': 24},
    {'name': 'Rapini', 'calories': 22},
    {'name': 'Ras Malai', 'calories': 331},
    {'name': 'Raspberry', 'calories': 52},
    {'name': 'Ravioli', 'calories': 143},
    {'name': 'Red Leaf Lettuce', 'calories': 14},
    {'name': 'Red Lentils', 'calories': 116},
    {'name': 'Ribeye Steak', 'calories': 291},
    {'name': 'Rice Milk', 'calories': 47},
    {'name': 'Rice Pudding', 'calories': 118},
    {'name': 'Ricotta Cheese', 'calories': 174},
    {'name': 'Ritz Cracker', 'calories': 80},
    {'name': 'Roast Beef', 'calories': 147},
    {'name': 'Romaine Lettuce', 'calories': 17},
    {'name': 'Romanesco', 'calories': 25},
    {'name': 'Root Beer', 'calories': 152},
    {'name': 'Rosemary', 'calories': 131},
    {'name': 'Roti', 'calories': 297},
    {'name': 'Rutabaga', 'calories': 37},
    {'name': 'Rye Bread', 'calories': 259},
    {'name': 'Safflower Oil', 'calories': 884},
    {'name': 'Saffron', 'calories': 310},
    {'name': 'Sage', 'calories': 315},
    {'name': 'Salami', 'calories': 336},
    {'name': 'Salmon', 'calories': 208},
    {'name': 'Salsify', 'calories': 82},
    {'name': 'Salsola', 'calories': 33},
    {'name': 'Saltine Cracker', 'calories': 433},
    {'name': 'Samosa', 'calories': 262},
    {'name': 'Samphire', 'calories': 20},
    {'name': 'Sandwich', 'calories': 250},
    {'name': 'Sardine', 'calories': 208},
    {'name': 'Sardines in Oil', 'calories': 208},
    {'name': 'Sausage Biscuit with Egg', 'calories': 530},
    {'name': 'Sausage Biscuit', 'calories': 450},
    {'name': 'Sausage Burrito', 'calories': 300},
    {'name': 'Sausage McMuffin with Egg', 'calories': 480},
    {'name': 'Sausage McMuffin', 'calories': 400},
    {'name': 'Sausage', 'calories': 301},
    {'name': 'Scallop', 'calories': 111},
    {'name': 'Scone', 'calories': 370},
    {'name': 'Seaweed', 'calories': 45},
    {'name': 'Serrano Pepper', 'calories': 32},
    {'name': 'Sesame Oil', 'calories': 884},
    {'name': 'Sesame', 'calories': 573},
    {'name': 'Shallot', 'calories': 72},
    {'name': 'Shiitake Mushroom', 'calories': 34},
    {'name': 'Shrimp', 'calories': 99},
    {'name': 'Side Salad', 'calories': 15},
    {'name': 'Sirloin Steak', 'calories': 218},
    {'name': 'Skim Milk', 'calories': 34},
    {'name': 'Smoothie', 'calories': 130},
    {'name': 'Snow Peas', 'calories': 42},
    {'name': 'Soba', 'calories': 200},
    {'name': 'Soft Baked Oatmeal Raisin Cookie', 'calories': 150},
    {'name': 'Sorbet', 'calories': 130},
    {'name': 'Sorrel', 'calories': 21},
    {'name': 'Sourdough Bread', 'calories': 174},
    {'name': 'Southwest Grilled Chicken Salad', 'calories': 350},
    {'name': 'Soy Milk', 'calories': 54},
    {'name': 'Soybeans', 'calories': 446},
    {'name': 'Spaghetti Squash', 'calories': 31},
    {'name': 'Spaghetti', 'calories': 158},
    {'name': 'Spam', 'calories': 174},
    {'name': 'Spicy Buffalo Sauce', 'calories': 10},
    {'name': 'Spinach', 'calories': 23},
    {'name': 'Split Peas', 'calories': 118},
    {'name': 'Sports Drink', 'calories': 50},
    {'name': 'Spring Roll', 'calories': 100},
    {'name': 'Squid', 'calories': 175},
    {'name': 'Star Anise', 'calories': 337},
    {'name': 'Starfruit', 'calories': 31},
    {'name': 'Steak', 'calories': 271},
    {'name': 'Stir Fry', 'calories': 200},
    {'name': 'Strawberry Banana Smoothie', 'calories': 210},
    {'name': 'Strawberry Shake (Small)', 'calories': 540},
    {'name': 'Strawberry', 'calories': 32},
    {'name': 'Sugar Snap Peas', 'calories': 42},
    {'name': 'Sunchokes', 'calories': 73},
    {'name': 'Sundae', 'calories': 280},
    {'name': 'Sunflower Oil', 'calories': 884},
    {'name': 'Sunflower Seeds', 'calories': 584},
    {'name': 'Sushi', 'calories': 350},
    {'name': 'Swede', 'calories': 37},
    {'name': 'Sweet \'N Sour Sauce', 'calories': 50},
    {'name': 'Sweet and Sour Pork', 'calories': 221},
    {'name': 'Sweet Potato', 'calories': 86},
    {'name': 'Sweet Tea (Small)', 'calories': 90},
    {'name': 'Swiss Chard', 'calories': 19},
    {'name': 'Swiss Cheese', 'calories': 380},
    {'name': 'Swordfish', 'calories': 172},
    {'name': 'Taco', 'calories': 226},
    {'name': 'Tamale', 'calories': 285},
    {'name': 'Tangerine', 'calories': 53},
    {'name': 'Taro Root', 'calories': 142},
    {'name': 'Tarragon', 'calories': 295},
    {'name': 'Tartar Sauce', 'calories': 70},
    {'name': 'Tater Tots', 'calories': 262},
    {'name': 'Tatsoi', 'calories': 18},
    {'name': 'Tatume Squash', 'calories': 16},
    {'name': 'Tea', 'calories': 2},
    {'name': 'Tempura', 'calories': 323},
    {'name': 'Tenderloin Steak', 'calories': 194},
    {'name': 'Teriyaki Chicken', 'calories': 282},
    {'name': 'Thyme', 'calories': 101},
    {'name': 'Tikka Masala', 'calories': 230},
    {'name': 'Tilapia', 'calories': 96},
    {'name': 'Tiramisu', 'calories': 240},
    {'name': 'Tomato Juice', 'calories': 17},
    {'name': 'Tomato', 'calories': 18},
    {'name': 'Tortellini', 'calories': 336},
    {'name': 'Tortilla Chips', 'calories': 489},
    {'name': 'Tortilla', 'calories': 218},
    {'name': 'Trail Mix', 'calories': 462},
    {'name': 'Tres Leches Cake', 'calories': 258},
    {'name': 'Triple Bacon Cheeseburger', 'calories': 780},
    {'name': 'Triple Big Mac', 'calories': 950},
    {'name': 'Triple Cheeseburger', 'calories': 520},
    {'name': 'Triple Hamburger', 'calories': 630},
    {'name': 'Triple McChicken', 'calories': 760},
    {'name': 'Triple McDouble', 'calories': 750},
    {'name': 'Triple McRib', 'calories': 960},
    {'name': 'Triple Quarter Pounder with Cheese', 'calories': 970},
    {'name': 'Trout', 'calories': 148},
    {'name': 'Tuna', 'calories': 132},
    {'name': 'Turban Squash', 'calories': 34},
    {'name': 'Turkey Breast', 'calories': 135},
    {'name': 'Turkey Jerky', 'calories': 451},
    {'name': 'Turkey Sandwich', 'calories': 250},
    {'name': 'Turkey Thigh', 'calories': 179},
    {'name': 'Turmeric', 'calories': 312},
    {'name': 'Turnip Greens', 'calories': 32},
    {'name': 'Turnip', 'calories': 28},
    {'name': 'Udon', 'calories': 310},
    {'name': 'Vanilla Cone', 'calories': 200},
    {'name': 'Vanilla Shake (Small)', 'calories': 500},
    {'name': 'Vegetable Juice', 'calories': 17},
    {'name': 'Vietnamese Coriander', 'calories': 23},
    {'name': 'Vindaloo', 'calories': 240},
    {'name': 'Walnut Oil', 'calories': 884},
    {'name': 'Walnuts', 'calories': 654},
    {'name': 'Watercress', 'calories': 11},
    {'name': 'Watermelon', 'calories': 30},
    {'name': 'White Bread', 'calories': 266},
    {'name': 'Whole Milk', 'calories': 61},
    {'name': 'Whole Wheat Bread', 'calories': 247},
    {'name': 'Wild Rice', 'calories': 101},
    {'name': 'Wonton', 'calories': 42},
    {'name': 'Yogurt', 'calories': 59},
    {'name': 'Yucca Root', 'calories': 160},
    {'name': 'Zephyr Squash', 'calories': 19},
    {'name': 'Zucchini', 'calories': 17},

]


#Sorting of foods alphabetically
foods.sort(key=lambda x: x['name'].lower())


#Defining Katch McArdle calculation method
def KatchMcArdle(weight, bodyfat):
    weight = weight * 0.453592
    LeanBodyMass = ((weight * (100 - bodyfat)) / 100)
    BasicMetabolicRate = 370 + (21.6 * LeanBodyMass)
    return BasicMetabolicRate


#Defining Mifflin-St Jeor calculation method
def MifflinStJeor(weight, height, age, gender):
    weight = weight * 0.453592
    height = height * 2.54
    if gender == "male":
        BasicMetabolicRate = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        BasicMetabolicRate = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return BasicMetabolicRate


#Calories per day based on previous calculations with activity levels
def calBurnedPerDay(BasicMetabolicRate, activitylevel):
    if activitylevel == "sedentary":
        IdealCalorieIntake = BasicMetabolicRate * 1.2
    elif activitylevel == "lightly active":
        IdealCalorieIntake = BasicMetabolicRate * 1.375
    elif activitylevel == "moderately active":
        IdealCalorieIntake = BasicMetabolicRate * 1.55
    else:
        IdealCalorieIntake = BasicMetabolicRate * 1.725
    IdealCalorieIntake = round(IdealCalorieIntake)
    return IdealCalorieIntake


#Homescreen button
@app.route('/')
def home():
    return render_template('home.html')


#Food calorie list
@app.route('/food_list', methods=['GET', 'POST'])
def food_list():
    search_query = request.form.get('search', '')

    #Search bar
    filtered_foods = []
    if search_query:
        for food in foods:
            if search_query.lower() in food['name'].lower():
                filtered_foods.append(food)
    else:
        filtered_foods = foods

    return render_template('food_list.html', foods=filtered_foods, search_query=search_query)


#Request for calorie calculations
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        calc_choice = request.form['calc_choice']
        weight = int(request.form['weight'])
        BasicMetabolicRate = 0

        
        if calc_choice == "Katch-McArdle":
            bodyfat = int(request.form['bodyfat'])
            BasicMetabolicRate = KatchMcArdle(weight, bodyfat)
        elif calc_choice == "Mifflin-St Jeor":
            height = int(request.form['height'])
            age = int(request.form['age'])
            gender = request.form['gender'].lower()
            BasicMetabolicRate = MifflinStJeor(weight, height, age, gender)

        
        activitylevel = request.form['activitylevel'].lower()
        IdealCalorieIntake = calBurnedPerDay(BasicMetabolicRate, activitylevel)

        
        #Displaying results
        return render_template('result.html', calorie_intake=IdealCalorieIntake)

    return render_template('index.html')


#Port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)