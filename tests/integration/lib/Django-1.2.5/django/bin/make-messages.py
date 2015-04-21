#!/usr/bin/env python

if __name__ == "__main__":
    import sys
    name = sys.argv[0]
    args = ' '.join(sys.argv[1:])
    print("%s has been moved into django-admin.py" % name, file=sys.stderr)
    print('Please run "django-admin.py makemessages %s" instead.'% args, file=sys.stderr)
    print(file=sys.stderr)
    sys.exit(1)

