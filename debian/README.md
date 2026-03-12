# Implicit operations

- `qlever-ui.service` is added by dh_installsystemd and automatically enabled and started after installation
- The `qlever-ui.(postinst|postrm|prerm)` files are installed by dh_installdeb
- `qlever-ui.lograte` is installed by dh_installlogrotate

- In the future we could use dh_installsysusers to create the users.
