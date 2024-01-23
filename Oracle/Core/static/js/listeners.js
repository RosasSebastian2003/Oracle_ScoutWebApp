

function fetchData(data) {
    return fetch('filter/events/teams/?option=' + data)
    .then(response => response.json())
    .then(data => 
            {
               var events = data.events;
               var teams = data.teams; 

               return {events, teams};
            }
         );
}

function populateStatesDropdown(event, dropdown) {    
    var state_option = document.createElement('a');
    state_option.value = event.fields.state_prov;
    state_option.text = event.fields.state_prov;
    state_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';

    dropdown.appendChild(state_option);
    
}

function populateCitiesDropdown(event, dropdown) {
    var city_option = document.createElement('a');
    city_option.value = event.fields.city;
    city_option.text = event.fields.city;
    city_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';

    dropdown.appendChild(city_option);
}

function populateEventsDropdown(event, dropdown) {
    var event_option = document.createElement('a');
    event_option.value = event.pk;
    event_option.text = event.fields.name;
    event_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';

    dropdown.appendChild(event_option);
}

function populateTeamsDropdown(team, dropdown) {
    var team_option = document.createElement('a');
    team_option.value = team.pk;
    team_option.text = team.pk;
    team_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';

    dropdown.appendChild(team_option);
}

function initializeCountryListener(dropdowns) {
    // Listen for changes in the dropdown, event parameter is handed by the browser

    dropdowns['country_dropdown'].addEventListener('click', function(event) {
        event.preventDefault();
        const target = event.target;

        var selectedCountry = target.getAttribute('value');
        console.log(`Country Dropdown Triggered, Selected Country: ${selectedCountry}`);

        dropdowns['state_dropdown'].innerHTML = ''; // State Dropdown
        dropdowns['city_dropdown'].innerHTML = ''; // City Dropdown
        dropdowns['event_dropdown'].innerHTML = ''; // Event Dropdown
        dropdowns['team_dropdown'].innerHTML = ''; // Team Dropdown

        // HTTP request to get the event objects for the selected country
        fetchData(selectedCountry).then(({events, teams}) => {
            // Repeat counters
            let state_list = new Set();
            let city_list = new Set();
            let team_list = new Set();

            events.forEach(event => {
                if (!state_list.has(event.fields.state_prov)) {
                    state_list.add(event.fields.state_prov);
                    populateStatesDropdown(event, dropdowns['state_dropdown']);
                }

                if (!city_list.has(event.fields.city)) {
                    city_list.add(event.fields.city);
                    populateCitiesDropdown(event, dropdowns['city_dropdown']);
                }

                populateEventsDropdown(event, dropdowns['event_dropdown']);

                teams.forEach(team => {
                    if (!team_list.has(team.pk)) {
                        team_list.add(team.pk);
                        populateTeamsDropdown(team, dropdowns['team_dropdown']);
                    }
                });
            });
        });

    });
}

function initializeStateListener(dropdowns) {
    dropdowns['state_dropdown'].addEventListener('change', function() {
        var selectedState = this.value;

        dropdowns['city_dropdown'].innerHTML = ''; // City Dropdown
        dropdowns['event_dropdown'].innerHTML = ''; // Event Dropdown
        dropdowns['team_dropdown'].innerHTML = ''; // Team Dropdown

        fetchData(selectedState).then(({events, teams}) => {
            // Repeat counters
            let city_list = new Set();
            let team_list = new Set();

            events.forEach(event => {
                if (!city_list.has(event.fields.city)) {
                    city_list.add(event.fields.city);
                    populateCitiesDropdown(event, dropdowns['city_dropdown']);
                }

                populateEventsDropdown(event, dropdowns['event_dropdown']);

                teams.forEach(team => {
                    if (!team_list.has(team.pk)) {
                        team_list.add(team.pk);
                        populateTeamsDropdown(team, dropdowns['team_dropdown']);
                    }
                });
            });
        });
    });
}

function initializeCityListener(dropdowns) {
    dropdowns['city_dropdown'].addEventListener('change', function() {
        var selectedCity = this.value;

        dropdowns['event_dropdown'].innerHTML = ''; // Event Dropdown
        dropdowns['team_dropdown'].innerHTML = ''; // Team Dropdown

        fetchData(selectedCity).then(({events, teams}) => {
            // Repeat counters
            let team_list = new Set();

            events.forEach(event => {
                populateEventsDropdown(event, dropdowns['event_dropdown']);

                teams.forEach(team => {
                    if (!team_list.has(team.pk)) {
                        team_list.add(team.pk);
                        populateTeamsDropdown(team, dropdowns['team_dropdown']);
                    }
                });
            });
        });
    });
}

function initializeEventListener(dropdowns) {
    dropdowns['event_dropdown'].addEventListener('change', function() {
        var selectedEvent = this.value;

        dropdowns['team_dropdown'].innerHTML = ''; // Team Dropdown

        // HTTP request to get the event objects for the selected country
        fetchData(selectedEvent).then(({_, teams}) => {
            // Repeat counters
            let team_list = new Set();

            teams.forEach(team => {
                if (!team_list.has(team.pk)) {
                    team_list.add(team.pk);
                    populateTeamsDropdown(team, dropdowns['team_dropdown']);
                }
            });
        });
    });
}


window.onload = function() {
    let dropdowns = {};

    dropdowns['country_dropdown'] = document.getElementById("country_dropdown");
    dropdowns['state_dropdown'] = document.getElementById("state_dropdown");
    dropdowns['city_dropdown'] = document.getElementById("city_dropdown");
    dropdowns['event_dropdown'] = document.getElementById("event_dropdown");
    dropdowns['team_dropdown'] = document.getElementById("team_dropdown");

    initializeCountryListener(dropdowns);
    initializeStateListener(dropdowns);
    initializeCityListener(dropdowns);
    initializeEventListener(dropdowns);
}