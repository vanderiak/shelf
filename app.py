from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def dash():
    recent_books_data = [
        {'title': 'Great Expectations', 'author': 'Dickens', 'height': 92, 'width': 56, 'color': '#34495e', 'author_color': 'rgb(170, 210, 255, 0.7)'},
        {'title': 'Pride & Prejudice', 'author': 'Austen', 'height': 88, 'width': 40, 'color': '#e0f2f7', 'author_color': 'rgb(107, 114, 128)'},
        {'title': 'The Scarlet Letter', 'author': None, 'height': 86, 'width': 40, 'color': '#708090', 'author_color': None},
        {'title': 'Moby Dick', 'author': 'Melville', 'height': 95, 'width': 48, 'color': '#2c3e50', 'author_color': 'rgb(170, 210, 255)'},
        {'title': 'War and Peace', 'author': 'Tolstoy', 'height': 98, 'width': 56, 'color': '#1f2937', 'author_color': 'rgba(229, 231, 235, 0.6)'},
        {'title': 'The Great Gatsby', 'author': 'Fitzgerald', 'height': 91, 'width': 48, 'color': '#34495e', 'author_color': 'rgb(96, 165, 250)'},
        {'title': '1984', 'author': 'Orwell', 'height': 89, 'width': 40, 'color': '#7f8c8d', 'author_color': 'rgb(229, 231, 235)'},
        {'title': 'Mockingbird', 'author': 'Lee', 'height': 90, 'width': 44, 'color': '#f39c12', 'author_color': 'rgb(146, 64, 14)'},
        {'title': 'Catcher in the Rye', 'author': None, 'height': 87, 'width': 36, 'color': '#c0392b', 'author_color': None},
        {'title': 'The Hobbit', 'author': 'Tolkien', 'height': 85, 'width': 44, 'color': '#27ae60', 'author_color': 'rgb(167, 243, 208)'},
        {'title': 'Jane Eyre', 'author': None, 'height': 93, 'width': 40, 'color': '#95a5a6', 'author_color': None},
        {'title': 'Little Women', 'author': 'Alcott', 'height': 89, 'width': 44, 'color': '#e74c3c', 'author_color': 'rgb(251, 207, 232)'},
        {'title': 'FRANKENSTEIN', 'author': None, 'height': 91, 'width': 40, 'color': '#2c3e50', 'author_color': None},
        {'title': 'Ulysses', 'author': 'James Joyce', 'height': 96, 'width': 56, 'color': '#3498db', 'author_color': 'rgb(191, 219, 254)'},
        {'title': 'Don Quixote', 'author': None, 'height': 94, 'width': 48, 'color': '#964b00', 'author_color': None},
        {'title': 'The Odyssey', 'author': 'Homer', 'height': 92, 'width': 40, 'color': '#e67e22', 'author_color': 'rgb(254, 215, 170)'},
        {'title': 'DRACULA', 'author': None, 'height': 88, 'width': 36, 'color': '#1e272e', 'author_color': None},
        {'title': 'Les Misérables', 'author': 'Hugo', 'height': 97, 'width': 48, 'color': '#2980b9', 'author_color': 'rgb(147, 197, 253)'},
        {'title': 'Walden', 'author': 'Thoreau', 'height': 90, 'width': 40, 'color': '#2ecc71', 'author_color': 'rgb(167, 243, 208)'},
        {'title': 'Cosmos', 'author': 'Sagan', 'height': 91, 'width': 48, 'color': '#1e293b', 'author_color': 'rgb(148, 163, 184)'},
        {'title': 'Silent Spring', 'author': 'Carson', 'height': 88, 'width': 40, 'color': '#16a085', 'author_color': 'rgb(153, 246, 228)'},
        {'title': 'Brief History of Time', 'author': 'Hawking', 'height': 93, 'width': 48, 'color': '#34495e', 'author_color': 'rgb(168, 162, 158)'},
        {'title': 'The Gene', 'author': 'Mukherjee', 'height': 91, 'width': 44, 'color': '#27ae60', 'author_color': 'rgb(134, 239, 172)'},
        {'title': 'Sapiens', 'author': 'Harari', 'height': 94, 'width': 56, 'color': '#f1c40f', 'author_color': 'rgb(146, 64, 14)'},
        {'title': 'Thinking, Fast & Slow', 'author': 'Kahneman', 'height': 92, 'width': 48, 'color': '#ecf0f1', 'author_color': 'rgb(100, 116, 139)'},
        {'title': 'Origin of Species', 'author': 'Darwin', 'height': 90, 'width': 48, 'color': '#34495e', 'author_color': 'rgb(217, 249, 157)'},
        {'title': 'Guns, Germs, Steel', 'author': None, 'height': 89, 'width': 44, 'color': '#7f8c8d', 'author_color': None},
        {'title': 'Relativity', 'author': 'Einstein', 'height': 86, 'width': 36, 'color': '#e74c3c', 'author_color': 'rgb(254, 202, 202)'},
        {'title': 'Principia Mathematica', 'author': 'Newton', 'height': 95, 'width': 56, 'color': '#34495e', 'author_color': 'rgb(251, 191, 36)'},
        {'title': 'Pale Blue Dot', 'author': None, 'height': 90, 'width': 40, 'color': '#2980b9', 'author_color': None},
        {'title': 'The Selfish Gene', 'author': 'Dawkins', 'height': 88, 'width': 40, 'color': '#1abc9c', 'author_color': 'rgb(167, 243, 208)'},
        {'title': 'Scientific Revolutions', 'author': None, 'height': 92, 'width': 44, 'color': '#95a5a6', 'author_color': None},
        {'title': 'The Code Breaker', 'author': 'Isaacson', 'height': 89, 'width': 48, 'color': '#e74c3c', 'author_color': 'rgb(251, 207, 232)'},
    ]
    stacked = [
        {'title': 'Astrophysics for People in a Hurry', 'author': None, 'height': 10, 'width': 36, 'color': '#8e44ad', 'author_color': None},
        {'title': 'Six Easy Pieces', 'author': None, 'height': 10, 'width': 32, 'color': '#c0392b', 'author_color': None},
        {'title': "Surely You're Joking", 'author': None, 'height': 8, 'width': 30, 'color': '#e67e22', 'author_color': None},
        {'title': 'Deep Work', 'author': None, 'height': 9, 'width': 36, 'color': '#34495e', 'author_color': None},
            ]

    stats_data = {
        'total_books': len(recent_books_data),
        'available_books': 9870,
        'on_loan_books': 1580,
        'overdue_books': 12,
        'recent_books': recent_books_data
    }

    return render_template('index.html', books=recent_books_data, stats=stats_data, stacks=stacked)

if __name__ == '__main__':
    app.run(debug=True)