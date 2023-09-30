import React, { useState } from "react";

const apiUrl = 'http://localhost:8000';

function UserIntake() {
  const [userInput, setUserInput] = useState('');
  const [aiResponse, setAiResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`${apiUrl}/generateTalkingPoints/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input_text: userInput }),
      });

      if (response.ok) {
        const data = await response.json();
        setAiResponse(data.aiResponse);
      } else {
        console.error('Error:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      {aiResponse && aiResponse.choices && aiResponse.choices.length > 0 && (
        <div>
          <h2>AI Response:</h2>
          <p>{aiResponse.choices[0].content}</p> {/* Display the content of the first choice */}
        </div>
      )}
    </div>
  );
}

export default UserIntake;
