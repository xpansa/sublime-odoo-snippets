Several snippets to be used with Sublime 3 in Odoo v8 developments

## Installation

This plugin is not available in common Sublime repository, you will need to add the repository which contains the plugin first.

### The repository

1. Goto **Preferences**->**Package Control**
1. Click in **Add Repository**
1. Adds the following URL: [https://github.com/sotogarcia/sublime-odoo-snippets](https://github.com/sotogarcia/sublime-odoo-snippets) and press **enter**.

### The pluggin

1. Goto **Preferences**->**Package Control**
1. Click in **Install package**
1. Search **sublime-odoo-snippets** plugin in list and **click** it.


> Plugin setup proccess requires **[Sublime Text](http://www.sublimetext.com/)** with **[Package Control](https://packagecontrol.io/installation)** installed.


## Snippets available

Following is a list of current available snippets in the project:

### Python

The scripts listed below can be used only in Python files:

#### base

- **openerp**: adds a basic file header and most used python imports
- **\_\_openerp\_\_**: adds a manifest file dictionary

#### Models

- **_inherit**: adds an _inherit attribute with a single element list.
- **_inherits**: adds an _inherits attribute with a single relationship.
- **models.Model**: adds a basic model declaration.
- **modelsearch**: adds a common code to search records from given model
- **modelbrowse**: adds a common code to search records from given model

#### Field declarations

- **fields-Binary**: adds a fields.Binary declaration
- **fields-Boolean**: adds a fields.Boolean declaration
- **fields-Char**: adds a fields.Char declaration
- **fields-Date**: adds a fields.Date declaration
- **fields-Datetime**: adds a fields.Datetime declaration
- **fields-Float**: adds a fields.Float declaration
- **fields-Html**: adds a fields.Html declaration
- **fields-Many2many**: adds a fields.M2m declaration
- **fields-Many2one**: adds a fields.M2o declaration
- **fields-One2many**: adds a fields.O2m declaration
- **fields-Reference**: adds a fields.Reference declaration
- **fields-Selection**: adds a fields.Selection declaration
- **fields-Text**: adds a fields.Text declaration

#### Field attributes
- **default**: adds a field default attribute with a lambda function.
- **search**: adds a field default attribute with a lambda function.
- **track_visibility**: adds a field track_visibility with *onchange* by default.

#### Field methods

- **defcompute**: adds a basic compute method declaration.
- **defonchange**: adds a basic onchange method declaration.
- **defsearch**: adds a basic search method declaration.

#### Model overwrittten methods

- **defcreate**: adds a basic overwrite declaration for create method.
- **defwrite**: adds a basic overwrite declaration for write method.
- **defunlink**: adds a basic overwrite declaration for unlink method.
- **defcopy**: adds a basic overwrite declaration for copy method.

#### Test

- **TransactionCase**: add a Transaction case inherited class

### XML

The scripts listed below can be used only in XML files:

#### base

- **openerp**: adds a most common XML tags used in Odoo files

#### Field declarations

- **fields-Binary**: adds a fields.Binary declaration
- **fields-Boolean**: adds a fields.Boolean declaration
- **fields-Char**: adds a fields.Char declaration
- **fields-Date**: adds a fields.Date declaration
- **fields-Datetime**: adds a fields.Datetime declaration
- **fields-Float**: adds a fields.Float declaration
- **fields-Html**: adds a fields.Html declaration
- **fields-Many2many**: adds a fields.M2m declaration
- **fields-Many2one**: adds a fields.M2o declaration
- **fields-One2many**: adds a fields.O2m declaration
- **fields-Reference**: adds a fields.Reference declaration
- **fields-Selection**: adds a fields.Selection declaration
- **fields-Text**: adds a fields.Text declaration

#### Actions

- **ir.actions.act_window**: adds XML record with model attribute set to *ir.actions.act_window*
- **ir.actions.act_window.view**:  adds XML record with model attribute set to *ir.actions.act_window.view*
- **ir.actions.report.xml**:  adds XML record with model attribute set to *ir.actions.report.xml*
- **ir.actions.server**:  adds XML record with model attribute set to *ir.actions.server*
- **ir.actions.todo**: adds XML record with model attribute set to *ir.actions.todo*

#### Views

- **ir.ui.view**: adds XML record with model attribute set to *ir.ui.view*
- **tree**: adds a new tree tag with attributes
- **form**: adds a new form tag with attributes
- **graph**: adds a new graph tag with attributes
- **search**: adds a new search tag with attributes
- **filter**: adds a new filter tag with attributes
- **field**: adds a new field tag
- **xpath**: adds a new xpath tag with attributes
- **attrs**: adds a new attribute *attrs* in tag
- **oe_chatter**: adds a new track area to be used inside a form tag

#### Security

- **ir.model.data**: adds XML record with model attribute set to *ir.model.data*
- **ir.rule**: adds XML record with model attribute set to *ir.rule*
- **res.groups**: adds XML record with model attribute set to *res.groups*

#### Data

- **ir.module.category**: adds XML record with model attribute set to *ir.module.category*
- **product.product**: adds XML record with model attribute set to *product.product*
- **product.template**: adds XML record with model attribute set to *product.template*
- **email.template**: adds an email template XML definition.

#### Others

- **ir.values**: : adds XML record with model attribute set to *ir.values*
- **base.action.rule**: adds XML record with model attribute set to *base.action.rule*
- **id-reference**: adds an evaluable expresion to get a resource database id from XML

#### Undocumented

- data\ir.model.data.sublime-snippet
- data\ir.model.sublime-snippet
- views\others\ir.filters.sublime-snippet
- views\others\ir.ui.menu.sublime-snippet
- views\others\object-button.sublime-snippet
- views\others\object-menuitem.sublime-snippet
- views\others\record.sublime-snippet

- strftime: views\others\strftime
- relativedelta: views\others\relativedelta
- attribute: views\ir.ui.view-xpath-attribute

- t: report-qweb-container

## Commands

Project has a Python file with some useful utilities to work in Odoo code files, these are follo

### dashes

When a Python code file is too long, reorder the code in blocks divided by horizontal rules makes more easy read them.

This command replaces selection by a dashed line with selected text in center. The result is like the following:

```python
    # ------------------------------- PRUEBA ----------------------------------
```

- Line starts at the selection beginning and ends in the column 79.
- Text will have two spaces, one before and another after.
- If there is not selected text when command is invoked, line will be printed without any text.

### finddashes

Once the Python code file has been divided by horizoantal rules, will be very useful to jump to the next line of dashes. This command does just that.
