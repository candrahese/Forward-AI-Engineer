import asyncio

class AIAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    async def complete_task(self, task):
        print(f"[{self.name}] Acting as {self.role}, working on: {task}")
        await asyncio.sleep(1)
        return f"Result from {self.name}: Task '{task}' completed."

async def run_orchestration():
    planner = AIAgent("Planner", "Strategic Architect")
    executor = AIAgent("Executor", "Code Specialist")
    
    # Sequential execution pattern
    plan = await planner.complete_task("Design a scalable AI schema")
    result = await executor.complete_task(f"Implement code based on: {plan}")
    
    print(f"Final Orchestration Result: {result}")

if __name__ == "__main__":
    asyncio.run(run_orchestration())