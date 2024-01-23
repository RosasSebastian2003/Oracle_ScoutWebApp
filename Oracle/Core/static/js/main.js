// Your code goes here
function filterEventsTeams(dropdownId) {
    var selectedOption = this.selectedOption;

    fetch('filter/events/teams/?option=' + selectedOption)
        .then(response => response.json())  
        .then(data => {
            var events = data.events;
            var teams = data.teams;
            var eventSelect = document.getElementById('event');
            var teamSelect = document.getElementById('team');

            eventSelect.innerHTML = '';
            teamSelect.innerHTML = '';
            
            switch (dropdownId) {
                case "country_dropdown":
                    let state_list = [];

                    events.forEach(event => {
                        if (!state_list.includes(event.state_prov)) {
                            state_list.push(event.state_prov);
                            var option = document.createElement('option');
                            option.value = event.state_prov;
                            option.text = event.state_prov;
                            option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                            eventSelect.appendChild(option);
                        }
                    });
                    break;
                
                case "state_dropdown":
                    let city_list = [];

                    events.forEach(event => {
                        if (!city_list.includes(event.city)) {
                            city_list.push(event.name);
                            var option = document.createElement('option');
                            option.value = event.city;
                            option.text = event.city;
                            option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                            eventSelect.appendChild(option);
                        }
                    });
                    break;
                case "city_dropdown":
                    events.forEach(event => {
                            var option = document.createElement('option');
                            option.value = event.city;
                            option.text = event.city;
                            option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                            eventSelect.appendChild(option);
                    });
                    break;
                    
                case "event_dropdown":
                    teams.forEach(team => {
                        var option = document.createElement('option');
                        option.value = team.team_number;
                        option.text = team.team_number;
                        option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                        teamSelect.appendChild(option);
                    });
                    break;
            }

        }
    );
}

