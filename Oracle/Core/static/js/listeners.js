
function initializeCountryListener() {
    // Get the dropdown element through its ID
    var country_dropdown = document.getElementById("country_dropdown");

    // Listen for changes in the dropdown
    country_dropdown.addEventListener('click', function(event) {
        event.preventDefault();
        const target = event.target;

        var selectedCountry = target.getAttribute('value');

        // Get the state dropdown element through its ID
        var state_dropdown = document.getElementById("state_dropdown");
        state_dropdown.innerHTML = '';

        // Get the city dropdown element through its ID
        var city_dropdown = document.getElementById("city_dropdown");
        city_dropdown.innerHTML = '';

        // Get the event dropdown element through its ID
        var event_dropdown = document.getElementById("event_dropdown");
        event_dropdown.innerHTML = '';

        // Get the team dropdown element through its ID
        var team_dropdown = document.getElementById("team_dropdown");
        team_dropdown.innerHTML = '';

        // HTTP request to get the event objects for the selected country
        fetch('filter/events/teams/?option=' + selectedCountry)
        .then(response => response.json())
        .then(data => {
            var events = data.events;
            var teams = data.teams;

            // Lists for locations
            let state_list = [];
            let city_list = [];
            let team_list = [];

            // Populate the all dropdowns
            events.forEach(event => {
                if (!state_list.includes(event.fields.state_prov)) {
                    state_list.push(event.fields.state_prov);

                    var state_option = document.createElement('a');
                    state_option.value = event.fields.state_prov;
                    state_option.text = event.fields.state_prov;
                    state_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';

                    state_dropdown.appendChild(state_option);
                }

                if (!city_list.includes(event.fields.city)) {
                    city_list.push(event.fields.city);

                    var city_option = document.createElement('a');
                    city_option.value = event.fields.city;
                    city_option.text = event.fields.city;
                    city_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                    city_dropdown.appendChild(city_option);
                }

                var event_option = document.createElement('a');
                event_option.value = event.pk;
                event_option.text = event.fields.name;
                event_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                event_dropdown.appendChild(event_option);

                teams.forEach(team => {
                    if (!team_list.includes(team.pk)) {
                        team_list.push(team.pk);

                        var team_option = document.createElement('a');
                        team_option.value = team.pk;
                        team_option.text = team.pk;
                        team_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                        team_dropdown.appendChild(team_option);
                    }
                });
            });
        });

    });
};

function initializeStateListener() {
    var state_dropdown = document.getElementById("state_dropdown");
    
    state_dropdown.addEventListener('change', function() {
        var selectedState = this.value;

        // Get the city dropdown element through its ID
        var city_dropdown = document.getElementById("city_dropdown");
        city_dropdown.innerHTML = '';

        // Get the state dropdown element through its ID
        var event_dropdown = document.getElementById("event_dropdown");
        event_dropdown.innerHTML = '';

        // HTTP request to get the event objects for the selected country
        fetch('filter/events/cities/?option=' + selectedState)
        .then(response => response.json())
        .then(data => {
            var events = data.events;
            var teams = data.teams;

            // Lists for locations
            let city_list = [];
            let team_list = [];

            // Populate the all dropdowns
            events.forEach(event => {
                if (!city_list.includes(event.city)) {
                    city_list.push(event.city);

                    var city_option = document.createElement('option');
                    city_option.value = event.city;
                    city_option.text = event.city;
                    city_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                    city_dropdown.appendChild(city_option);

                    var event_option = document.createElement('option');
                    event_option.value = event.key;
                    event_option.text = event.name;
                    event_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                    event_dropdown.appendChild(event_option);

                    teams.forEach(team => {
                        if (!team_list.includes(team.team_number)) {
                            team_list.push(team.team_number);

                            var team_option = document.createElement('option');
                            team_option.value = team.team_number;
                            team_option.text = team.team_number;
                            team_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                            team_dropdown.appendChild(team_option);
                        }
                    });
                }
            });
        });
    });
};

function initializeCityListener() {
    var city_dropdown = document.getElementById("city_dropdown");

    city_dropdown.addEventListener('change', function() {
        var selectedCity = this.value;

        // Get the state dropdown element through its ID
        var event_dropdown = document.getElementById("event_dropdown");
        event_dropdown.innerHTML = '';

        // HTTP request to get the event objects for the selected country
        fetch('filter/events/events/?option=' + selectedCity)
        .then(response => response.json())
        .then(data => {
            var events = data.events;
            var teams = data.teams;

            // Lists for locations
            let team_list = [];

            // Populate the all dropdowns
            events.forEach(event => {
                var event_option = document.createElement('option');
                event_option.value = event.key;
                event_option.text = event.name;
                event_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                event_dropdown.appendChild(event_option);

                teams.forEach(team => {
                    if (!team_list.includes(team.team_number)) {
                        team_list.push(team.team_number);

                        var team_option = document.createElement('option');
                        team_option.value = team.team_number;
                        team_option.text = team.team_number;
                        team_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                        team_dropdown.appendChild(team_option);
                    }
                });
            });
        });
    });
};

function initializeEventListener() {
    var event_dropdown = document.getElementById("event_dropdown");

    event_dropdown.addEventListener('change', function() {
        var selectedEvent = this.value;

        // Get the state dropdown element through its ID
        var team_dropdown = document.getElementById("team_dropdown");
        team_dropdown.innerHTML = '';

        // HTTP request to get the event objects for the selected country
        fetch('filter/events/teams/?option=' + selectedEvent)
        .then(response => response.json())
        .then(data => {
            var teams = data.teams;

            // Lists for locations
            let team_list = [];

            // Populate the all dropdowns
            teams.forEach(team => {
                if (!team_list.includes(team.team_number)) {
                    team_list.push(team.team_number);

                    var team_option = document.createElement('option');
                    team_option.value = team.team_number;
                    team_option.text = team.team_number;
                    team_option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                    team_dropdown.appendChild(team_option);
                }
            });
        });
    });
};


window.onload = function() {
    initializeCountryListener();
    initializeStateListener();
    initializeCityListener();
    initializeEventListener();
}