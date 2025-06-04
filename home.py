import ar_master
from flask import Flask, render_template, flash, request, session, current_app, send_from_directory, redirect, url_for
from flask import jsonify
app = Flask(__name__, static_folder="static")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
mm = ar_master.master_flask_code()





@app.route("/")
def homepage():
    news_items = mm.select_direct_query("SELECT message FROM news ORDER BY id DESC")
    return render_template('index.html', news_items=news_items)


@app.route("/pdo_view")
def pdo_view():
    return render_template('pdo_view.html')



@app.route("/admin")
def admin():
    return render_template('admin.html')


@app.route("/admin_log", methods = ['GET', 'POST'])
def admin_log():
    error = None

    if request.method == 'POST':
        un = request.form['uname']
        pa = request.form['pass']
        print(un)
        print(pa)
        pa = pa.strip()
        un = un.strip()
        if un == "admin" and pa == "admin":
            return render_template('admin_home.html', error=error)
        else:
            return render_template('admin.html',flash_message = True, data="error")
    return render_template("admin.html")



@app.route("/pdo_add_family_member", methods = ['GET', 'POST'])
def pdo_add_family_member():
    area=session['area']
    if request.method == 'POST':
        family_head_name = request.form['family_head_name']
        family_head_aadhar_no = request.form['family_head_aadhar_no']
        ration_card_no = request.form['ration_card_no']
        family_member_count = request.form['family_member_count']
        family_members_name = request.form['family_members_name']
        members_eligible_for_vote = request.form['members_eligible_for_vote']
        door_no = request.form['door_no']
        street = request.form['street']
        area = request.form['area']
        village = request.form['village']
        post = request.form['post']
        taluk = request.form['taluk']
        district = request.form['district']

        maxin = mm.find_max_id("family_members_details")
        qq = "INSERT INTO family_members_details (id, family_head_name, family_head_aadhar_no, ration_card_no, family_member_count, members_eligible_for_votes, votes_cast, door_no, street, area, village, post, taluk, district, status) VALUES ('" + str(maxin) + "','" + str(family_head_name) + "','" + str(
    family_head_aadhar_no) + "','" + str(ration_card_no) + "','" + str(family_member_count) + "','" + str(members_eligible_for_vote) + "','0','" + str(door_no) + "','" + str(
    street) + "','" + str(area) + "','" + str(village) + "','" + str(post) + "','" + str(taluk) + "','" + str(district) + "','0')"

        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('pdo_add_family_member.html',flash_message = True, data="Success")
        else:
            return render_template('pdo_add_family_member.html',flash_message = True, data="Failed")
    return render_template('pdo_add_family_member.html',area=area)


@app.route("/pdo_add_service", methods = ['GET', 'POST'])

def pdo_add_service():
    area=session['area']
    if request.method == 'POST':
        pdo=session['user']
        area=session['area']
        service_name = request.form['service_name']
        service_date = request.form['service_date']
        maxin = mm.find_max_id("service_details")
        qq = "insert into service_details values('" + str(maxin) + "','" + str(service_name) + "','" + str(service_date) + "','" + str(pdo) + "','0','"+str(area)+"')"
        result = mm.insert_query(qq)
        if (result == 1):
            return render_template('pdo_add_service.html',flash_message = True, data="Success")
        else:
            return render_template('pdo_add_service.html',flash_message = True, data="Failed")
    return render_template('pdo_add_service.html',area=area)



@app.route("/pdo_add_fine", methods = ['GET', 'POST'])
def pdo_add_fine():
    if request.method == 'POST':
        pdo=session['user']
        family_head_name = request.form['family_head_name']
        fine_regarding = request.form['fine_regarding']
        fine_amount = request.form['fine_amount']
        fine_date = request.form['fine_date']
        maxin = mm.find_max_id("fine_details")
        qq = "insert into fine_details values('" + str(maxin) + "','" + str(family_head_name) + "','" + str(fine_regarding) + "','" + str(fine_amount) + "','" + str(fine_date) + "','" + str(pdo) + "','0','0')"
        result = mm.insert_query(qq)
        if (result == 1):
            return render_template('pdo_add_fine.html', flash_message = True, data="Success")
        else:
            return render_template('pdo_add_fine.html',flash_message = True, data="Failed")
    return render_template('pdo_add_fine.html')


@app.route("/staff_login")
def staff_login():
    return render_template('staff_login.html')

@app.route("/admin_home")
def admin_home():
    return render_template('admin_home.html')




@app.route("/admin_add_pdo", methods = ['GET', 'POST'])
def admin_add_pdo():
    if request.method == 'POST':
        pdo_name = request.form['pdo_name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        gender = request.form['gender']
        username = request.form['username']
        password = request.form['password']
        maxin = mm.find_max_id("pdo_details")
        qq = "insert into pdo_details values('" + str(maxin) + "','" + str(pdo_name) + "','" + str(contact) + "','" + str(
                email) + "','" + str(address) + "','" + str(gender) + "','" + str(username) + "','" + str(password) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('admin_add_pdo.html',flash_message = True, data=" PDO Details Added Successfully")
        else:
            return render_template('admin_add_pdo.html')
    return render_template('admin_add_pdo.html')



@app.route("/pdo", methods = ['GET', 'POST'])
def pdo():
    msg = None
    if request.method == 'POST':
        n = request.form['username']
        g = request.form['password']

        n1 = str(n)
        g1 = str(g)

        q = ("SELECT * from pdo_details where username='" + str(n1) + "' and password='" + str(g1) + "'")
        data = mm.select_direct_query(q)
        data1=data



        data = len(data)
        if data == 0:
            return render_template('pdo.html', flash_message=True, data="Failed")
        else:
            session['area'] = data1[0][4]
            # print(data1[0][4])
            msg = 'Success'
            session['user'] = n
            return render_template('pdo_home.html', sid=n)
    return render_template('pdo.html', error=msg)




@app.route("/pdo_home")
def pdo_home():
    user_home = 1
    return render_template('pdo_home.html',user_home=user_home)

def value(): 
    voting_stats= mm.insert_query("SELECT status FROM voting_status")
    return voting_stats
@app.route("/get_voting_status", methods=['GET'])
def get_voting_status():
   
    v = mm.select_direct_query("SELECT status FROM voting_status")
    # l = mm.select_direct_query("SELECT members_eligible_for_votes,votes_cast FROM family_members_details where family_head_name='user '")
    # print(l)
    voting_status = v[0][0] if v else 0
    session['voting_status'] = voting_status  # Keep session in sync
    return jsonify({'voting_status': voting_status})

@app.route("/user", methods = ['GET', 'POST'])
def user():
    msg = None
    if request.method == 'POST':
        n = request.form['username']
        g = request.form['password']
    
        n1 = str(n)
        g1 = str(g)

        q = ("SELECT * from user_details where username='" + str(n1) + "' and password='" + str(g1) + "'")
        v = ("SELECT status FROM voting_status")
        data = mm.select_direct_query(q)
        data1 = mm.select_direct_query(q)

        data = len(data)
        if data == 0:
            return render_template('user.html', flash_message=True, data="Failed")
        else:
            area = data1[0][3]
            session['area'] = area
            msg = 'Success'
            session['user'] = n
        
            return render_template('user_home.html')
    return render_template('user.html', error=msg)



@app.route("/user_register", methods = ['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        gender = request.form['gender']
        contact = request.form['contact']
        username = request.form['username']
        password = request.form['password']
        maxin = mm.find_max_id("user_details")
        qq = "insert into user_details values('" + str(maxin) + "','" + str(name) + "','" + str(email) + "','" + str(
                address) + "','" + str(gender) + "','" + str(contact) + "','" + str(username) + "','" + str(password) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('user.html', flash_message = True, data="Success")
        else:
            return render_template('user_register.html')
    return render_template('user_register.html')



@app.route("/user_home")
def user_home():
    user_home=1
    return render_template("user_home.html",user_home=user_home)



@app.route("/pdo_view_family_details")
def pdo_view_family_details():
    area = session['area']
    data=mm.select_direct_query("select * from family_members_details where status='0' and district='"+str(area)+"'")
    return render_template('pdo_view_family_details.html',items=data)


@app.route("/admin_view_user")
def admin_view_user():
    data=mm.select_direct_query("select id, name, email, address, LOWER(gender) from user_details")
    return render_template('admin_view_user.html',items=data)



@app.route("/admin_pdo_details")
def admin_pdo_details():
    data=mm.select_direct_query("select * from pdo_details")
    return render_template('admin_pdo_details.html',items=data)


@app.route("/admin_pdo_details_edit/<string:id>")
def admin_pdo_details_edit(id):
    session['id']=id
    data=mm.select_direct_query("select * from pdo_details where id='"+str(id)+"'")
    return render_template('admin_pdo_details_edit.html',items=data)



@app.route("/pdo_family_details_edit/<string:id>")
def pdo_family_details_edit(id):
    session['id']=id
    data=mm.select_direct_query("select * from family_members_details where id='"+str(id)+"'")
    return render_template('pdo_family_details_edit1.html',items=data)




@app.route("/pdo_family_details_delete/<string:id>")
def pdo_family_details_delete(id):
    session['id']=id
    mm.insert_query("delete  from family_members_details where id='"+str(id)+"'")
    return pdo_view_family_details()



@app.route("/admin_pdo_details_delete/<string:id>")
def admin_pdo_details_delete(id):
    session['id']=id
    mm.insert_query("delete  from pdo_details where id='"+str(id)+"'")
    return admin_pdo_details()


@app.route("/pdo_family_details_edit1", methods = ['GET', 'POST'])
def pdo_family_details_edit1():
    id=session['id']
    if request.method == 'POST':
        family_head_name = request.form['family_head_name']
        family_head_aadhar_no = request.form['family_head_aadhar_no']
        ration_card_no = request.form['ration_card_no']
        members_eligible_for_vote = request.form['members_eligible_for_vote']
        family_member_count = request.form['family_member_count']
        family_members_name = request.form['family_members_name']
        door_no = request.form['door_no']
        street = request.form['street']
        area = request.form['area']
        village = request.form['village']
        post = request.form['post']
        taluk = request.form['taluk']
        district = request.form['district']
         # Corrected SQL Query
        qq = f"""
        UPDATE family_members_details 
        SET family_head_name = '{family_head_name}',
            family_head_aadhar_no = '{family_head_aadhar_no}',
            ration_card_no = '{ration_card_no}',
            family_member_count = '{family_member_count}',
            members_eligible_for_votes = '{members_eligible_for_vote}',
            door_no = '{door_no}',
            street = '{street}',
            area = '{area}',
            village = '{village}',
            post = '{post}',
            taluk = '{taluk}',
            district = '{district}'
        WHERE id = '{id}'
        """
        print(qq)
        result = mm.insert_query(qq)

        if (result == 1):
            return pdo_view_family_details()
        else:
            return render_template('pdo_view_family_details.html',flash_message = True, data='Failed')
    return render_template('pdo_view.html')





@app.route("/admin_pdo_details_edit1", methods = ['GET', 'POST'])
def admin_pdo_details_edit1():
    id=session['id']
    if request.method == 'POST':
        pdo_name = request.form['pdo_name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        gender = request.form['gender']
        username = request.form['username']
        password = request.form['password']
        maxin = mm.find_max_id("pdo_details")
        qq = "update  pdo_details set pdo_name='" + str(pdo_name) + "',contact='" + str(contact) + "',email='" + str(
                email) + "',address='" + str(address) + "',gender='" + str(gender) + "',username='" + str(username) + "',password='" + str(password) + "' where id='"+str(id)+"'"
        print(qq)
        result = mm.insert_query(qq)

        if (result == 1):
            return admin_pdo_details()
        else:
            return render_template('admin_home.html',flash_message = True, data='Failed')
    return render_template('admin_home.html')


@app.route("/admin_add_scheme", methods = ['GET', 'POST'])
def admin_add_scheme():
    if request.method == 'POST':
        scheme_name = request.form['scheme_name']
        scheme_eligibility_criteria = request.form['scheme_eligibility_criteria']
        age = request.form['age']
        description = request.form['description']
        govenment = request.form['govenment']

        maxin = mm.find_max_id("scheme_details")
        qq = "insert into scheme_details values('" + str(maxin) + "','" + str(scheme_name) + "','" + str(scheme_eligibility_criteria) + "','" + str(
                age) + "','" + str(description) + "','" + str(govenment) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('admin_add_scheme.html', flash_message = True, data="Success")
        else:
            return render_template('admin_add_scheme.html')
    return render_template('admin_add_scheme.html')




@app.route("/pdo_applied_users")
def pdo_applied_users():

    area = session['area']
    # data = mm.select_direct_query("select * from fine_details where family_head_name='" + str(user) + "' and status='0'")
    qry = "select user_apply_scheme.id,user_apply_scheme.uname,user_apply_scheme.status,scheme_details.* from user_apply_scheme,scheme_details where user_apply_scheme.status='1' and user_apply_scheme.scheme_id=scheme_details.id and user_apply_scheme.area='"+str(area)+"'"
    print(qry)
    data = mm.select_direct_query(qry)
    return render_template('pdo_applied_users.html',items=data)



@app.route("/user_pay_fine")
def user_pay_fine():
    user=session['user']
    data=mm.select_direct_query("select * from fine_details where family_head_name='"+str(user)+"' and status='0'")

    return render_template('user_pay_fine.html',items=data)




@app.route("/user_pay_fine_1/<string:id>")
def user_pay_fine_1(id):
    session['id']=id
    # mm.insert_query("update fine_details set status='1' where id='"+str(id)+"'")
    return render_template('user_pay_fine_1.html')



@app.route("/user_pay_fine_2", methods = ['GET', 'POST'])
def user_pay_fine_2():
    id=session['id']
    if request.method == 'POST':
        from datetime import date
        today = date.today()

        mm.insert_query("update fine_details set status='1',report='"+str(today)+"' where id='"+str(id)+"'")
    return render_template('user_home.html', flash_message = True, data="Payment Success")




@app.route("/user_add_complaint", methods = ['GET', 'POST'])
def user_add_complaint():
    uname=session['user']
    area=session['area']
    if request.method == 'POST':
        from datetime import date
        today = date.today()
        complaint_description = request.form['complaint_description']
        complaint_on = request.form['complaint_on']

        maxin = mm.find_max_id("user_complaint_details")
        qq = "insert into user_complaint_details values('" + str(maxin) + "','" + str(uname) + "','" + str(complaint_description) + "','" + str(
                complaint_on) + "','0','0','"+str(today)+"','"+str(area)+"')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('user_add_complaint.html', flash_message = True, data="Success")
        else:
            return render_template('admin_add_scheme.html')
    return render_template('user_add_complaint.html')




@app.route("/user_add_death_birth", methods = ['GET', 'POST'])
def user_add_death_birth():
    uname = session['user']
    area = session['area']
    from datetime import date
    today = date.today()
    if request.method == 'POST':
        person_name = request.form['person_name']
        type = request.form['type']
        radiobutton = request.form['gender']
        date = request.form['date']
        time = request.form['time']

        maxin = mm.find_max_id("death_birth_details")
        qq = "insert into death_birth_details values('" + str(maxin) + "','" + str(uname) + "','" + str(person_name) + "','" + str(
                type) + "','" + str(radiobutton) + "','" + str(date) + "','" + str(time) + "','0','0','"+str(today)+"','"+str(area)+"')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('user_add_death_birth.html', flash_message = True, data="Success")
        else:
            return render_template('user_add_death_birth.html')
    return render_template('user_add_death_birth.html')





@app.route("/user_payment_history")
def user_payment_history():
    user=session['user']
    data=mm.select_direct_query("select * from fine_details where family_head_name='"+str(user)+"' and status='1'")
    return render_template('user_payment_history.html',items=data)



@app.route("/user_view_scheme")
def user_view_scheme():
    user=session['user']
    area=session['area']
    data=mm.select_direct_query("select * from scheme_details")
    return render_template('user_view_scheme.html',items=data)



@app.route("/user_view_service")
def user_view_service():
    user=session['user']
    area=session['area']
    data=mm.select_direct_query("select * from service_details")
    return render_template('user_view_service.html',items=data)





@app.route("/pdo_view_payment")
def pdo_view_payment():
    data=mm.select_direct_query("select * from fine_details where status='1'")
    return render_template('pdo_view_payment.html',items=data)




@app.route("/pdo_view_complaint")
def pdo_view_complaint():
    area=session['area']
    data=mm.select_direct_query("select * from user_complaint_details where status='0' and area='"+str(area)+"'")
    return render_template('pdo_view_complaint.html',items=data)



@app.route("/pdo_view_complaint_1/<string:id>")
def pdo_view_complaint_1(id):
    session['id']=id
    # mm.insert_query("update fine_details set status='1' where id='"+str(id)+"'")
    return render_template('pdo_view_complaint_1.html')



@app.route("/pdo_view_complaint_2", methods = ['GET', 'POST'])
def pdo_view_complaint_2():
    if request.method == 'POST':
        action = request.form['action']
        id=session['id']
        mm.insert_query("update user_complaint_details set status='1',report='"+str(action)+"' where id='" + str(id) + "'")
    # return render_template('pdo_view_complaint_1.html')pdo_view_complaint
    # return redirect(url_for('pdo_view_complaint_3', flashMessage=True,data='Success'))
    return render_template('pdo_view.html', flash_message=True,data='Success')


@app.route("/pdo_view_action")
def pdo_view_action():
    data=mm.select_direct_query("select * from user_complaint_details where status='1'")
    return render_template('pdo_view_action.html',items=data)



@app.route("/pdo_view_death_birth")
def pdo_view_death_birth():
    area=session['area']
    data=mm.select_direct_query("select * from death_birth_details where status='0' and area='"+str(area)+"'")
    return render_template('pdo_view_death_birth.html',items=data)



@app.route("/pdo_view_death_birth_1/<string:id>")
def pdo_view_death_birth_1(id):
    session['id']=id
    mm.insert_query("update death_birth_details set status='1' where id='"+str(id)+"'")
    return render_template('pdo_view.html', flash_message=True,data='Success')




@app.route("/pdo_view_scheme_details")
def pdo_view_scheme_details():
    qry="select user_apply_scheme.id,user_apply_scheme.uname,user_apply_scheme.status,scheme_details.* from user_apply_scheme,scheme_details where user_apply_scheme.status='0' and user_apply_scheme.scheme_id=scheme_details.id"
    print(qry)
    data=mm.select_direct_query(qry)
    return render_template('pdo_view_scheme_details.html',items=data)



@app.route("/user_view_scheme_1/<string:id>")
def user_view_scheme_1(id):
    uname=session['user']
    area=session['area']
    from datetime import date
    today = date.today()

    # data=mm.select_direct_query("select * from scheme_details where id='"+str(id)+"'")
    maxin=mm.find_max_id("user_apply_scheme")
    mm.insert_query("insert into user_apply_scheme values('"+str(maxin)+"','"+str(uname)+"','"+str(id)+"','0','"+str(today)+"','"+str(area)+"')")
    return render_template('user_home.html', flash_message=True,data='Success')



@app.route("/pdo_view_scheme_details_1/<string:id>")
def pdo_view_scheme_details_1(id):
    session['id']=id
    mm.insert_query("update user_apply_scheme set status='1' where id='"+str(id)+"'")
    return render_template('pdo_home.html', flash_message=True,data='Success')


@app.route("/user_applied_users")
def user_applied_users():
    qry="select user_apply_scheme.uname,user_apply_scheme.status,scheme_details.* from user_apply_scheme,scheme_details where  user_apply_scheme.status='1' and user_apply_scheme.scheme_id=scheme_details.id"
    print(qry)
    data=mm.select_direct_query(qry)
    return render_template('user_applied_users.html',items=data)



@app.route("/admin_view_request")
def admin_view_request():
    qry="select user_apply_scheme.id,user_apply_scheme.uname,user_apply_scheme.status,scheme_details.* from user_apply_scheme,scheme_details where user_apply_scheme.status='1' and user_apply_scheme.scheme_id=scheme_details.id"
    print(qry)
    data=mm.select_direct_query(qry)
    return render_template('admin_view_request.html',items=data)



@app.route("/pdo_view_report")
def pdo_view_report():

    return render_template('pdo_view_report.html')



@app.route("/pdo_view_report_1", methods = ['GET', 'POST'])
def pdo_view_report_1():
    if request.method == 'POST':
        date = request.form['date']
        area=session['area']
        qq="select * from fine_details,user_details where fine_details.report='"+str(date)+"' and user_details.address='"+str(area)+"' and fine_details.family_head_name=user_details.name"
        # print(qq)
        fine_data=mm.select_direct_query(qq)
        death_birth_data=mm.select_direct_query("select * from death_birth_details where cdate='"+str(date)+"' and area='"+str(area)+"'")
        qry = "select user_apply_scheme.id,user_apply_scheme.uname,user_apply_scheme.status,scheme_details.* from user_apply_scheme,scheme_details where user_apply_scheme.status='1' and user_apply_scheme.scheme_id=scheme_details.id and user_apply_scheme.area='" + str(
            area) + "' and user_apply_scheme.report='"+str(date)+"'"
        # print(qry)
        user_scheme=mm.select_direct_query(qry)
        user_complaint=mm.select_direct_query("select * from user_complaint_details where date='"+str(date)+"' and area='"+str(area)+"' and status='1'")

        return render_template('pdo_view_report_1.html',fine_data=fine_data,death_birth_data=death_birth_data,user_scheme=user_scheme,user_complaint=user_complaint)
    return render_template('pdo_view_report.html')


# from flask import Flask, render_template, request, session, redirect, url_for, flash
# import ar_master

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
# mm = ar_master.master_flask_code()

# User Suggestion Page
@app.route("/user_suggestion", methods=['GET', 'POST'])
def user_suggestion():
    user = session.get('user', 'Guest')
    if request.method == 'POST':
        village = request.form['village']
        date = request.form['date']
        message = request.form['message']
        max_id = mm.find_max_id("suggestions")
        
        query = f"INSERT INTO suggestions VALUES('{max_id}', '{user}', '{village}', '{date}', '{message}', '0', '0')"
        result = mm.insert_query(query)
        
        if result == 1:
            flash("Suggestion submitted successfully!", "success")
            return redirect(url_for('user_suggestion'))
        else:
            flash("Failed to submit suggestion.", "danger")
    
    return render_template("user_suggestion.html")

# PDO View Suggestions
@app.route("/pdo_view_suggestions")
def pdo_view_suggestions():
    suggestions = mm.select_direct_query("SELECT * FROM suggestions WHERE status='0'")
    return render_template("pdo_view_suggestions.html", items=suggestions)

# Clear Suggestion (PDO Action)
@app.route("/pdo_clear_suggestion/<int:id>")
def pdo_clear_suggestion(id):
    from datetime import date
    today = date.today()
    
    query = f"UPDATE suggestions SET status='1', viewed_date='{today}' WHERE id='{id}'"
    mm.insert_query(query)
    
    # Notify User
    suggestion = mm.select_direct_query(f"SELECT user FROM suggestions WHERE id='{id}'")[0]
    user = suggestion[0]
    max_notif_id = mm.find_max_id("notifications")
    notification = f"INSERT INTO notifications VALUES('{max_notif_id}','{user}', 'Your Suggestion is Viewed by PDO', '{today}')"
    mm.insert_query(notification)

        
    flash("Suggestion marked as viewed.", "info")
    return redirect(url_for('pdo_view_suggestions'))


# User Notifications Page
@app.route("/user_notifications")
def user_notifications():
    user = session.get('user', 'Guest')
    notifications = mm.select_direct_query2("SELECT message, date FROM notifications WHERE user=%s ORDER BY date DESC", (user,))
    return render_template("user_notifications.html", notifications=notifications)

# Admin - Post News
@app.route("/admin_news", methods=['GET', 'POST'])
def admin_news():
    if request.method == 'POST':
        news_message = request.form['news_message']
        max_id = mm.find_max_id("news")
        query = "INSERT INTO news (id, message) VALUES (%s, %s)"
        mm.insert_query2(query, (max_id, news_message))
        flash("News posted successfully!", "success")
        return redirect(url_for('admin_news'))
    
    news_items = mm.select_direct_query("SELECT * FROM news ORDER BY id DESC")
    return render_template("admin_news.html", news_items=news_items)

# Admin - Edit News
@app.route("/admin_edit_news/<int:id>", methods=['GET', 'POST'])
def admin_edit_news(id):
    if request.method == 'POST':
        updated_message = request.form['news_message']
        query = "UPDATE news SET message=%s WHERE id=%s"
        mm.insert_query2(query, (updated_message, id))
        flash("News updated successfully!", "info")
        return redirect(url_for('admin_news'))
    
    news_item = mm.select_direct_query2("SELECT * FROM news WHERE id=%s", (id,))[0]
    return render_template("admin_edit_news.html", news_item=news_item)

# Admin - Delete News
@app.route("/admin_delete_news/<int:id>")
def admin_delete_news(id):
    query = "DELETE FROM news WHERE id=%s"
    mm.insert_query2(query, (id,))
    flash("News deleted successfully!", "danger")
    return redirect(url_for('admin_news'))

# Admin - Delete Candidate
@app.route("/admin_delete_candidate/<int:id>")
def admin_delete_candidate(id):
    query = "DELETE FROM voting_candidates WHERE id=%s"
    mm.insert_query2(query, (id,))
    flash("Candidate deleted successfully!", "danger")
    return redirect(url_for('admin_add_candidate'))

@app.route("/admin_start_voting", methods=['GET', 'POST'])
def admin_start_voting():
    if request.method == 'POST':
        mm.insert_query("UPDATE voting_status SET status=1")
        flash("Voting has started!", "success")
    return redirect(url_for('admin_view_candidates'))

@app.route("/admin_stop_voting", methods=['GET', 'POST'])
def admin_stop_voting():
    if request.method == 'POST':
        mm.insert_query("UPDATE voting_status SET status=0")
        flash("Voting has stopped!", "danger")
    return redirect(url_for('admin_view_candidates'))

@app.route("/admin_add_candidate", methods=['GET', 'POST'])
def admin_add_candidate():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        maxin = mm.find_max_id("voting_candidates")
        mm.insert_query(f"INSERT INTO voting_candidates VALUES('{maxin}', '{name}', '{age}', '{position}', 0)")
        flash("Candidate added successfully!", "success")
    return render_template("admin_add_candidate.html")

@app.route("/admin_view_candidates")
def admin_view_candidates():
    candidates = mm.select_direct_query("SELECT * FROM voting_candidates")
    return render_template("admin_view_candidates.html", candidates=candidates)

# ---------------------- USER MODULE ---------------------- #

@app.route("/vote", methods=['GET', 'POST'])
def vote():
    voting_status = mm.select_direct_query("SELECT status FROM voting_status")[0][0]
    if voting_status == 0:
        return render_template("vote_closed.html")
    
    if request.method == 'POST':
        aadhaar = request.form['aadhaar']
        password = request.form['password']
        print(aadhaar, password)
        aadhar_check =[1 if( mm.select_direct_query2("SELECT * FROM family_members_details WHERE family_head_aadhar_no=%s", (aadhaar)) and mm.select_direct_query2("SELECT * FROM user_details WHERE  password=%s", (password))) else 0]
        print((aadhar_check)[0])
        if not (aadhar_check)[0]:
            print("Invalid Aadhaar or Password!")
            flash("Invalid Aadhaar or Password!", "danger")
            return redirect(url_for('vote'))
        
        session['aadhaar'] = aadhaar
        print("Login Successful!")
        user_data = mm.select_direct_query2("SELECT members_eligible_for_votes, votes_cast FROM family_members_details WHERE family_head_aadhar_no=%s", (aadhaar))
        if not user_data:
            flash("User data not found!", "danger")
            print("User data not found!")
            return redirect(url_for('vote'))
        
        max_votes, votes_cast = user_data[0]
        
        if votes_cast >= max_votes:
            flash("You have used all your votes!", "warning")
            return render_template("vote_closed.html")
        
        candidates = mm.select_direct_query("SELECT * FROM voting_candidates")
        return render_template("vote.html", candidates=candidates, votes_remaining=max_votes-votes_cast)

    return render_template("vote_login.html")

@app.route("/submit_vote", methods=['POST'])
def submit_vote():
    if 'aadhaar' not in session:
        return redirect(url_for('vote'))
    
    aadhaar = session['aadhaar']
    candidate_id = request.form['candidate_id']
    
    user_data = mm.select_direct_query2("SELECT members_eligible_for_votes, votes_cast FROM family_members_details WHERE family_head_aadhar_no=%s", (aadhaar,))
    max_votes, votes_cast = user_data[0]
    
    if votes_cast >= max_votes:
        flash("You have used all your votes!", "warning")
        return render_template("vote_closed.html")
    
    mm.insert_query2("INSERT INTO voting_votes (user_aadhaar, candidate_id) VALUES (%s, %s)", (aadhaar, candidate_id))
    mm.insert_query2("UPDATE voting_candidates SET votes = votes + 1 WHERE id = %s", (candidate_id))
    mm.insert_query2("UPDATE family_members_details SET votes_cast = votes_cast + 1 WHERE family_head_aadhar_no = %s", (aadhaar))
    
    flash("Vote submitted successfully!", "success")
    return redirect(url_for('user_home'))


@app.route("/fetch_notifications")
def fetch_notifications():
    if 'user' not in session:
        return jsonify({"status": "error", "message": "User not logged in"})

    user = session['user']
    notifications = mm.select_direct_query2(
        "SELECT message, date FROM notifications WHERE user=%s ORDER BY date DESC", (user,)
    )
    total_notifications = len(notifications)

    return jsonify({"status": "success", "total_notifications": total_notifications, "notifications": notifications})

@app.route("/suggestion_vote")
def suggestion_vote():
    
    return render_template("suggestion_vote.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/get_chatbot_response", methods=['POST'])
def get_chatbot_response():
    if 'user' not in session:
        return jsonify({'status': 'error', 'response': 'Please log in to use the chatbot.'})

    user_message = request.json.get('message', '').strip()
    if not user_message:
        return jsonify({'status': 'error', 'response': 'Message cannot be empty.'})

    # Predefined responses
    intents = {
        "Fine Payment": "You can view and pay fines under the 'Pay Fine' section.",
        "Complaint": "To file a complaint, visit the 'Complaints' section and fill out the form.",
        "Birth Registration": "For birth registration, go to 'Death & Birth' in the sidebar.",
        "Death Registration": "For death registration, visit 'Death & Birth' in the menu.",
        "Payment History": "Check the 'Payment History' section for your past transactions.",
        "Government Schemes": "Visit the 'Schemes' section to view and apply for government schemes.",
        "Service Access": "Access various services under the 'Services' tab.",
        "Application Status": "You can track your scheme applications under 'Application Status'.",
        "Help": "I can assist you with fines, complaints, registrations, schemes, and more. What do you need help with?"
    }

    response = intents.get(user_message, "I'm sorry, I couldn't understand that. Please select a predefined option.")
    return jsonify({'status': 'success', 'response': response})

######################################
if __name__ == '__main__':
    # app.run(debug=True, use_reloader=True)
    app.run(host='0.0.0.0', port=4500,debug=True, use_reloader=True)