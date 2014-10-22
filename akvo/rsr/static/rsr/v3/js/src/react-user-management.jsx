/** @jsx React.DOM */

var Modal = ReactBootstrap.Modal;
var ModalTrigger = ReactBootstrap.ModalTrigger;
var Button = ReactBootstrap.Button;
var Table = ReactBootstrap.Table;

var ConfirmModal = React.createClass({
  deleteEmployment: function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: "DELETE",
        url: "/rest/v1/employment/" + this.props.employment.id + '/?format=json',
        success: function(data) {
            this.handleDelete();
        }.bind(this),
        error: function(xhr, status, err) {
            console.error(this.props.url, status, err.toString());
        }.bind(this)
    });
  },

  handleDelete: function() {
      this.props.onDeleteToggle();
  },

  render: function() {
    return this.transferPropsTo(
        <Modal title="Remove link to organisation">
          <div className="modal-body">
            {'Are you sure you want to remove the link to this organisation: ' + this.props.employment.organisation_name + '?'}
          </div>
          <div className="modal-footer">
            <Button onClick={this.props.onRequestHide}>Close</Button>
            <Button onClick={this.deleteEmployment} bsStyle="danger">Remove</Button>
          </div>
        </Modal>
      );
  }
});

var TriggerConfirmModal = React.createClass({
    render: function () {
        return (
            <ModalTrigger modal={<ConfirmModal employment={this.props.employment} onDeleteToggle={this.props.onDeleteToggle} />}>
                <Button bsStyle="danger" bsSize="xsmall">X</Button>
            </ModalTrigger>
            );
    }
});

var Employment = React.createClass({
    getInitialState: function() {
        return {visible: true};
    },

    onDelete: function() {
        this.setState({visible: false});
    },

    render: function() {
        return this.state.visible
            ? <li>{this.props.employment.organisation_name} <TriggerConfirmModal employment={this.props.employment} onDeleteToggle={this.onDelete} /></li>
            : <span/>;
    }
});

var EmploymentList = React.createClass({
    getInitialState: function() {
        return { employments: [] };
    },

    componentDidMount: function() {
        $.get(this.props.source, function(result) {
            var employments = result.results;
            if (this.isMounted()) {
                this.setState({
                    employments: employments
                });
            }
        }.bind(this));
    },

    render: function () {
        var employments = this.state.employments.map(function(employment) {
            return (
                <Employment employment={employment}/>
                )
        });
        return (
            <ul>{employments}</ul>
            );
    }
});

var UserRow = React.createClass({
    render: function() {
        return (
            <tr>
              <td>{this.props.user.email}</td>
              <td>{this.props.user.first_name}</td>
              <td>{this.props.user.last_name}</td>
              <td><EmploymentList source={"/rest/v1/employment/?format=json&user=" + this.props.user.id} /></td>
              <td><i>to do</i></td>
            </tr>
            );
    }
});

var UserTable = React.createClass({
    getInitialState: function() {
        return { users: [] };
    },

    componentDidMount: function() {
        $.get(this.props.source, function(result) {
            var users = result.results;
            if (this.isMounted()) {
                this.setState({
                    users: users
                });
            }
        }.bind(this));
      },

    render: function() {
        var users = this.state.users.map(function(user) {
          return (
            <UserRow user={user} />
          )
        });
        return (
            <Table striped>
                <thead><tr><th>Email</th><th>First name</th><th>Last name</th><th>Organisations</th><th>Permissions</th></tr></thead>
                <tbody>{users}</tbody>
            </Table>
            );
    }
});

React.renderComponent(<UserTable source="/rest/v1/user/?format=json" />, document.getElementById('user_table'));