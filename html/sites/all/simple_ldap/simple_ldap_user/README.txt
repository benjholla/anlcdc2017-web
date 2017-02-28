Simple LDAP User
================

This module allows authentication to the LDAP directory configured in the
Simple LDAP module. It also provides synchronization services both to and from
LDAP and Drupal. It supports mapping LDAP attributes to Drupal user object
fields (both native, and using Field API).

Configuration
=============

In addition to the configuration available in the administration UI, an
attribute map can be specified in settings.php, using the variable
$conf['simple_ldap_user_attribute_map'].

This variable is an array of arrays, where each of the arrays have the
following items:

* drupal - The field name on the Drupal user. This must be the machine name of
	   the field. To specify Field module fields, prefix the field name with a
	   hash, e.g. '#field_foo'. If no hash prefix is found, it is assumed that the
	   field is a property of the user itself, such as name, pass, mail, etc.

	   This can also be an array of drupal properties or fields. If the array
	   contains more than one entry, synchronization for that map only works in
	   the drupal->ldap direction, and the fields are concatenated with a space
	   separator.

	   Note: If you are mapping a Field module field that does not store its data
	   in a 'value' column, you need to specify the name of the column in the
	   mapping itself using square brackets. See the Country example below.

* ldap - The LDAP attribute on the LDAP user.

Example:
--------
$conf['simple_ldap_user_attribute_map'] = array(

  // Generic example.
  array(
    'drupal' => '#drupal-user-field-machine-name',
    'ldap' => 'ldap-attribute',
  ),

  // First name example.
  array(
    'drupal' => '#field_first_name',
    'ldap' => 'givenName',
  ),

  // Last name example.
  array(
    'drupal' => '#field_last_name',
    'ldap' => 'sn',
  ),

  // Country example.
  array(
    'drupal' => '#field_country[iso2]',
    'ldap' => 'localityName',
  ),

  // Timezone example (saved directly to users table, note there is no '#').
  array(
    'drupal' => 'timezone',
    'ldap' => 'l',
  ),

  // Combined fields example.
  array(
    'drupal' => array(
      '#field_first_name',
      '#field_last_name',
    ),
    'ldap' => 'displayName',
  ),

);

Active Directory Example:
-------------------------
$conf['simple_ldap_user_attribute_map'] = array(
  array(
    'drupal' => '#field_first_name',
    'ldap' => 'givenName',
  ),
  array(
    'drupal' => '#field_last_name',
    'ldap' => 'sn',
  ),
  array(
    'drupal' => array(
      '#field_first_name',
      '#field_last_name',
    ),
    'ldap' => 'CN',
  ),
  array(
    'drupal' => array(
      '#field_first_name',
      '#field_last_name',
    ),
    'ldap' => 'displayName',
  ),
);

Testing
=======

The simpletests provided with this module automatically configure themeselves
to use the active configuration in order to perform a real-world test against
your real LDAP server.

THIS MEANS THAT DATA WILL BE ADDED/DELETED ON YOUR REAL LDAP SERVER!

The simpletests only operate against entries it creates, but in the event of a
failure, the test cannot clean up after itself. If you are testing a specific
configuration, it is recommended to run the test against a development or
staging directory first.
