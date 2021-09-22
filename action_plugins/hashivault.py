from ansible.plugins.action import ActionBase
import yaml
import os.path


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        if task_vars is None:
            task_vars = dict()
            
        result = super(ActionModule, self).run(tmp, task_vars)

        creds_file = task_vars['infraunlimited_vault_admin_creds_file']

        if not os.path.exists(creds_file):
            args = self._task.args.copy()
            result.update(self._execute_module(module_args=args, task_vars=task_vars))
            return result

        with open(creds_file) as f:
            creds = yaml.safe_load(f)
        args = self._task.args.copy()
        if 'authtype' not in args:
            args['authtype'] = 'userpass'
        if 'url' not in args:
            args['url'] = creds['url']
        if 'username' not in args:
            args['username'] = creds['user']
        if 'password' not in args:
            args['password'] = creds['password']
        result.update(self._execute_module(module_args=args, task_vars=task_vars))
        return result
