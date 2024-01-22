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
                case 1:
                    events.forEach(event => {
                        var option = document.createElement('option');
                        option.value = event.id;
                        option.text = event.state_prov;
                        option.className = 'block px-4 py-2 text-gray-800 hover:bg-blue-500 hover:text-white';
                        eventSelect.appendChild(option);
                    });
                    break;
            }

        }
    );
}