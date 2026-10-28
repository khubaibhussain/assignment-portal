from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
# Error/Success messages dikhane ke liye secret key zaroori hai
app.secret_key = 'super_secret_key' 

# Valid submissions ko save karne ke liye ek simple list
submissions = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Form se data receive karna[cite: 1]
        name = request.form.get('name')
        reg_no = request.form.get('reg_no')
        title = request.form.get('title')
        url = request.form.get('url')

        # Validation 1: Koi required field khali nahi honi chahiye[cite: 1]
        if not name or not reg_no or not title or not url:
            flash('Error: Tamam fields fill karna zaroori hai!', 'error')
            return redirect(url_for('index'))

        # Validation 2: URL proper format mein hona chahiye[cite: 1]
        if not (url.startswith('http://') or url.startswith('https://')):
            flash('Error: Invalid submission URL. URL http:// ya https:// se start hona chahiye.', 'error')
            return redirect(url_for('index'))

        # Dono validations pass ho jayen toh submission save karein[cite: 1]
        submissions.append({
            'name': name,
            'reg_no': reg_no,
            'title': title,
            'url': url
        })
        flash('Success: Assignment submit ho gaya!', 'success')
        return redirect(url_for('index'))

    # Frontend par form aur saved submissions display karein[cite: 1]
    return render_template('index.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)