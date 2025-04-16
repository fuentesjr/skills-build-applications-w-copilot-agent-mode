import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://stunning-meme-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="card shadow mb-4">
      <div className="card-header d-flex justify-content-between align-items-center bg-info text-white">
        <h2 className="mb-0">Teams</h2>
        <button className="btn btn-light btn-sm fw-bold">+ Add Team</button>
      </div>
      <div className="card-body">
        <table className="table table-striped table-hover">
          <thead className="table-info">
            <tr>
              <th>Name</th>
              <th>Members</th>
            </tr>
          </thead>
          <tbody>
            {teams.map(team => (
              <tr key={team._id}>
                <td>{team.name}</td>
                <td>{Array.isArray(team.members) ? team.members.length : 0}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Teams;
