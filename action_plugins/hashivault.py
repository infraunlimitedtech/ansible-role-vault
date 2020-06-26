from ansible.plugins.action import ActionBase
from jinja2 import Template
import yaml
import os
import os.path


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        creds_filename_tmpl = task_vars['infraunlimited_vault_admin_creds_file']
        t = Template(creds_filename_tmpl)
        creds_file = t.render(task_vars)

        if not os.path.exists(creds_file):
            print(creds_file)
            self._display.warning('Can not find file with admin creds - %s. If next operations failed please check it first' % creds_file)
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
