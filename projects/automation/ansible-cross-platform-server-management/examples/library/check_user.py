#!/usr/bin/python3
"""Read-only account-existence check for Linux hosts."""
import pwd

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec={"username": {"type": "str", "required": True}},
        supports_check_mode=True,
    )
    username = module.params["username"]

    try:
        pwd.getpwnam(username)
        exists = True
    except KeyError:
        exists = False

    module.exit_json(
        changed=False,
        username=username,
        exists=exists,
        msg="Account exists" if exists else "Account not found",
    )


if __name__ == "__main__":
    main()
