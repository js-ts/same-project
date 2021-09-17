import logging
import azure.durable_functions as df


# Constants
EXECUTE_STEP_ACTIVITY_NAME = "execute_step"


def orchestrator_function(context: df.DurableOrchestrationContext):
    # Get all steps to execute
    steps = context.get_input()

    # TODO Determine which ones can be executed in parallel and construct the appropriate DAG
    # executions = []
    # for step in steps:
    #     execution = context.call_activity(EXECUTE_STEP_ACTIVITY_NAME, step)
    #     executions.append(execution)
    # results = yield context.task_all(executions)

    # Execute all steps one after the other
    # Note: Assume that the list of steps is in order of required (sequential) execution
    results = []
    for step in steps:
        result = yield context.call_activity(EXECUTE_STEP_ACTIVITY_NAME, step)
        results.append(result)

    return results


main = df.Orchestrator.create(orchestrator_function)
