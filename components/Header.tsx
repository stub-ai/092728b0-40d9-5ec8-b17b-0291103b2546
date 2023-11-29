import React from 'react';

const Header: React.FC = () => {
  return (
    <header className="p-4 bg-blue-500 text-white">
      <h1 className="text-xl">My App</h1>
      <select className="mt-2 bg-white text-black">
        <option value="">Select an option</option>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </select>
    </header>
  );
};

export default Header;