from . import app


@app.route('/ping')
def login():
    return 'Pong'


"""
@app.route('/upload', methods=['POST'])
def upload():
    form = CarForm()
    if form.validate_on_submit():
        if 'photo' in request.files:
            photo = request.files['photo']
            filename = secure_filename(photo.filename)
            path = '{0}/{1}'.format(app.config['UPLOAD_FOLDER'], filename)
            photo.save(path)
            car = Car(manufacturer=form.manufacturer.data,
                      model=form.model.data, year=form.year.data,
                      photo=filename)
            car.save()
            flash('New car added')
            return redirect(url_for('search'))
    url = url_for('cars')
    return render_template('cars.html', form=form, url=url)
"""
