# TehNet Backup and Restore Baseline

## Backup scope

- MariaDB database dump
- `wp-content/uploads/`
- custom `tehnet` theme
- `tehnet-core` plugin
- active Nginx vhost
- `wp-config.php` stored only in protected backup storage, never Git

## Minimum backup command

```bash
STAMP="$(date +%Y%m%d-%H%M%S)"
install -d -m 0700 /opt/tehnet/backups/$STAMP
mariadb-dump --single-transaction "$TEHNET_DB_NAME" > "/opt/tehnet/backups/$STAMP/database.sql"
tar -C /var/www/tehnet -czf "/opt/tehnet/backups/$STAMP/wp-content.tgz" wp-content wp-config.php
cp /etc/nginx/sites-available/tehnet.conf "/opt/tehnet/backups/$STAMP/nginx.conf"
sha256sum /opt/tehnet/backups/$STAMP/* > "/opt/tehnet/backups/$STAMP/SHA256SUMS"
```

Database credentials are supplied at execution time and are not stored in this repository.

## Restore validation

A restore test must target an isolated temporary database/path or staging host. Production is never overwritten merely to prove that a backup can be restored.
