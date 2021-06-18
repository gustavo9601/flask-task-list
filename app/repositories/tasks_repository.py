from app.models.task import Task, db

class TasksRepository:
    @classmethod
    def get_task_by_id(self, id) -> Task:
        task = Task.query.filter_by(id=id).first()
        return task

    @classmethod
    def get_all_tasks(self):
        tasks = Task.query.all()
        return tasks

    @classmethod
    def create_task(self, arguments):
        task = Task(**arguments)
        db.session.add(task)
        db.session.commit()
        return task

    @classmethod
    def destroy_task(self, id):
        task = Task.query.filter_by(id=id).first()
        db.session.delete(task)
        db.session.commit()
        return task


