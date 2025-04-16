import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://stunning-meme-8000.app.github.dev/api/users/')
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  return (
    <div className="card shadow mb-4">
      <div className="card-header d-flex justify-content-between align-items-center bg-secondary text-white">
        <h2 className="mb-0">Users</h2>
        <button className="btn btn-light btn-sm fw-bold">+ Add User</button>
      </div>
      <div className="card-body">
        <table className="table table-striped table-hover">
          <thead className="table-secondary">
            <tr>
              <th>Username</th>
              <th>Email</th>
            </tr>
          </thead>
          <tbody>
            {users.map(user => (
              <tr key={user._id}>
                <td>{user.username}</td>
                <td>{user.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Users;
