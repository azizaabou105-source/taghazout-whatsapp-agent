from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class TaghazoutAgency():
    """TaghazoutAgency crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def whatsapp_concierge(self) -> Agent:
        return Agent(
  config=self.agents_config['whatsapp_concierge'],
  verbose=True
        )

    @task
    def reply_whatsapp_task(self) -> Task:
        return Task(
  config=self.tasks_config['reply_whatsapp_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
  agents=self.agents,
  tasks=self.tasks,
  process=Process.sequential,
  verbose=True,
        )
