from flask import Flask, render_template, request, flash, redirect, url_for
from urllib.parse import urlparse

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Valid submissions ko save karne ke liye list
submissions = []

def is_valid_url(u):
    """URL validation to ensure proper scheme and domain syntax."""
    if not u:
        return False
    p = urlparse(u)
    return p.scheme in ('http', 'https') and bool(p.netloc) and '.' in p.netloc

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Form values get karna aur extra spaces khatam karna
        name = (request.form.get('name') or '').strip()
        reg_no = (request.form.get('reg_no') or '').strip()
        title = (request.form.get('title') or '').strip()
        url = (request.form.get('url') or '').strip()

        # Validation 1: Mandatory fields check (Only spaces wale input reject honge)
        if not name or not reg_no or not title or not url:
            flash('Error: Tamam fields fill karna zaroori hai!', 'error')
            return redirect(url_for('index'))

        # Validation 2: Proper domain URL validation check
        if not is_valid_url(url):
            flash('Error: Invalid submission URL.', 'error')
            return redirect(url_for('index'))

        # Valid submission save karein
        submissions.append({
            'name': name,
            'reg_no': reg_no,
            'title': title,
            'url': url
        })
        flash('Success: Assignment submit ho gaya!', 'success')
        return redirect(url_for('index'))

    return render_template('index.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)