def deliver_reminders(user, date):
    reminder_flag = False
    session = CognitionQuestionSessionModel.i_first(
        order_by=('-date',),
        user_id=user['user_id']
    )
    if session:
        objs = CognitionQuestionSessionModel.i_list(
            user_id=user['user_id'],
            date=session.date,
            status__in=[
                QuestionSession.ScheduleStatus.WAITING_ANSWER,
                QuestionSession.ScheduleStatus.WAITING_FEEDBACK
            ]
        )
        if objs:
            notification = CognitionQuestionNotification()
            notification.devivery_reminder(user['user_id'])
            add_reminder_history(user['user_id'], date, objs[0].question_id, objs[0].id)
            reminder_flag = True
    return reminder_flag 