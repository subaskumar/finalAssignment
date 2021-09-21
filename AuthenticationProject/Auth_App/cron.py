def my_cron_job():
    # your functionality goes here
    daily_users = User.objects.filter(date_joined__day=datetime.today().day).count()
    print("The number of SignUp Today is :",daily_users )
    return daily_users