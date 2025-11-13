from flask import Flask, render_template, request

app = Flask(__name__)

# --- Python Functions ---
def get_string_operations(name):
    return {
        "Uppercase": name.upper(),
        "Lowercase": name.lower(),
        "Reversed": name[::-1],
        "Length": len(name)
    }

def add_language(language_list, new_lang):
    if new_lang and new_lang not in language_list:
        language_list.append(new_lang.capitalize())
        return f"{new_lang.capitalize()} added successfully!"
    return "Invalid or duplicate language."

def delete_selected_languages(language_list, selected):
    if not selected:
        return "No languages selected for deletion."

    deleted = []
    for lang in selected:
        if lang in language_list:
            language_list.remove(lang)
            deleted.append(lang)

    if not deleted:
        return "No matching languages found."

    # Show names of deleted languages
    return f"Deleted: {', '.join(deleted)}"


def clear_languages(language_list):
    language_list.clear()
    return "All languages cleared!"

def sort_languages(language_list):
    language_list.sort()
    return "Languages sorted alphabetically!"

# --- Routes ---
@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    global languages
    if 'languages' not in globals():
        languages = ["Python", "C++", "JavaScript", "Go"]

    message = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            new_lang = request.form.get('language')
            message = add_language(languages, new_lang)

        elif action == 'delete_selected':
            selected = request.form.getlist('selected_languages')
            message = delete_selected_languages(languages, selected)

        elif action == 'clear':
            message = clear_languages(languages)

        elif action == 'sort':
            message = sort_languages(languages)

    return render_template(
        "favorites.html",
        title="Favorites",
        languages=languages,
        message=message
    )





# --- Flask route ---
@app.route('/favorites', methods=['GET', 'POST'])
def favorites_page():
    ...

    global languages
    if 'languages' not in globals():
        languages = ["Python", "C++", "JavaScript", "Go"]

    message = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            new_lang = request.form.get('language')
            message = add_language(languages, new_lang)

        elif action == 'delete_selected':
            selected = request.form.getlist('selected_languages')
            message = delete_selected_languages(languages, selected)

        elif action == 'clear':
            message = clear_languages(languages)

        elif action == 'sort':
            message = sort_languages(languages)

    return render_template(
        "favorites.html",
        title="Favorites",
        languages=languages,
        message=message
    )
if __name__ == '__main__':
    app.run(debug=True)