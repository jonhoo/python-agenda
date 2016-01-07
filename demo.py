#!/usr/bin/env python3
import agenda

agenda.section("Set up network")
agenda.task("Create Virtual Private Cloud")
agenda.task("Attach internet gateway")
agenda.task("Allocate subnet #1")
agenda.subtask("Hook in internet-enabled route table")
agenda.task("Allocate subnet #2")
agenda.task("Generate VPC key-pair")
agenda.subfailure("Could not create key-pair")
agenda.subtask("Attempting to delete old key-pair")
agenda.subtask("Attempting to generate new key-pair")

agenda.section("Launch instances")
agenda.task("Launch instances in cluster #1")
agenda.task("Launch instances in cluster #2")
agenda.task("Wait for HQ to start running")
agenda.subtask("Still in 'pending' state")
agenda.subtask("Still in 'pending' state")
agenda.task("Wait for workers to reach 'running' state")
agenda.task("Wait for HQ to become pingable")
print("54.84.179.156 | UNREACHABLE!")
print("54.84.179.156 | UNREACHABLE!")
print('54.84.179.156 | SUCCESS => {"changed": false, "ping": "pong"}')
agenda.task("Wait for workers to become pingable")
print('10.0.1.237 | SUCCESS => {"changed": false, "ping": "pong"}')

agenda.section("Deploy application")
print("""\
PLAY [ansible-playbook]
TASK [common : Run application]
fatal: [10.0.1.237]: FAILED! => {"changed": true, "cmd": ...}
PLAY RECAP
10.0.1.237: ok=6    changed=4    unreachable=0    failed=1""")
agenda.failure("Application failed to run correctly")

agenda.section("Clean up VPC")
agenda.prompt("Press [Enter] when you are ready to clean")
print("")  # input()
agenda.task("Terminate all instances")
agenda.subtask("At least one instance still shutting down")
agenda.subtask("At least one instance still shutting down")
agenda.task("Delete network resources")
agenda.subtask("key pair")
agenda.subtask("internet gateway")
agenda.subtask("subnets")
agenda.task("Delete the VPC")
