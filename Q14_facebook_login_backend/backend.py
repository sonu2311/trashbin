from flask_lib import FlaskLib

import os
import json



backend = FlaskLib()

def save_in_file(filename, obj):
	with open(filename, 'w') as fd:
		fd.write(json.dumps(obj))


def load_from_file(filename):
	if not os.path.isfile(filename):
		return None
	with open(filename) as fd:
		return json.loads(fd.read())


@backend.api('/bhens_sum_of_sonu')
def A(d):
    print(d)
    return 'Mera Nam Sonu Hai'

@backend.api('/sum2')
def A(d):
    print(d)
    return 'PPP'

@backend.api('/api/sum2')
def sum2(d):
    print(d)
    return d['x'] + d['y']

@backend.api('/api/multi')
def multi(d):
	return d['x']*d['y']

################################################
def email_check(email,l):
	for i in l:
		if i["email"]==email:
			return True
	return False

users_list=[]


@backend.api('/api/sign_up_api')
def sign_up_in_backend(d):
	print(d)
	if email_check(d['email'], users_list):
		return False
	else:
		users_list.append(d)
		return True

def email_password_check(email,password,l):
	for i in l:
		if i["email"]==email and i["password"]==password:
			return True
	return False

@backend.api('/api/login_api')
def login_in_backend(d):
	print(d)
	print(users_list)
	if email_password_check(d['email'],d['password'],users_list):
		return True
	else:
		return False

posts_list=load_from_file("posts.txt") or []

@backend.api('/api/post_api')
def post_in_backend(d):
	posts_list.append(d)
	save_in_file("posts.txt", posts_list)
	print(posts_list)

@backend.api('/api/facebook_mujhe_sare_post_ki_list_do')
def facebook_in_backend(d):
	return posts_list

@backend.api('/api/like_api')
def like_in_backend(d):
	posts_list[d['z']]['like'] += 1
	save_in_file("posts.txt", posts_list)
	return posts_list

@backend.api('/api/add_comment')
def add_comment_in_backend(d):
	posts_list[d['u']]['comments'].append(d['comment'])
	save_in_file("posts.txt", posts_list)
	return posts_list

backend.run(port=5502)
