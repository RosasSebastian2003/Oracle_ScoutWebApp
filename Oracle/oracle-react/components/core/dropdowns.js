import React, { useState} from 'react';

function CountryDropdown(props) {
  const [country, setCountry] = useState('US');
  const countries = ['US', 'UK', 'India', 'Australia', 'Canada'];
  return (
    <select value={country} onChange={e => setCountry(e.target.value)}>
      {countries.map((country, index) => (
        <option key={index} value={country}>
          {country}
        </option>
      ))}
    </select>
  );
}