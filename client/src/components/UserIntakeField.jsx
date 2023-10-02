import React, { useState } from 'react';
import axios from 'axios';

const UserIntake = () => {
  const apiUrl = 'http://localhost:8000/';
  const [inputText, setInputText] = useState('');
  const [generatedText, setGeneratedText] = useState('');
  const [error, setError] = useState('');

  const handleAiResponse = async () => {
    try {
      if (inputText.trim() === '') {
        setError('Input cannot be empty');
        return;
      }

      console.log(inputText);

      const response = await axios.post(`${apiUrl}generateTalkingPoints/`, { user_input: inputText }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      setGeneratedText(response.data.generated_text);
      setError('');
    } catch (error) {
      console.error('Error:', error);
      setError('An error occurred while fetching the response.');
    }
  };

  return (
    <div>
      <input type="text" value={inputText} onChange={(e) => setInputText(e.target.value)} />
      <button onClick={handleAiResponse}>Submit</button>
      {error && <div>{error}</div>}
      <div>
        <div>
          {inputText}
        </div>
        <div>{generatedText}</div>
      </div>
    </div>
  );
};

export default UserIntake;

// import React, { useState } from "react";

// const apiUrl = 'http://localhost:8000';

// function UserIntake() {
//   const [userInput, setUserInput] = useState('');
//   const [aiResponse, setAiResponse] = useState(null);

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     try {
//       const response = await fetch(`${apiUrl}/generateTalkingPoints/`, {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ input_text: userInput }),
//       });

//       if (response.ok) {
//         const data = await response.json();
//         setAiResponse(data.aiResponse);
//       } else {
//         console.error('Error:', response.status, response.statusText);
//       }
//     } catch (error) {
//       console.error('Error:', error);
//     }
//   };

//   return (
//     <div>
//       <form onSubmit={handleSubmit}>
//         <input
//           type="text"
//           value={userInput}
//           onChange={(e) => setUserInput(e.target.value)}
//         />
//         <button type="submit">Submit</button>
//       </form>
//       {aiResponse && aiResponse.choices && aiResponse.choices.length > 0 && (
//         <div>
//           <h2>AI Response:</h2>
//           <p>{aiResponse.choices[0].content}</p> {/* Display the content of the first choice */}
//         </div>
//       )}
//     </div>
//   );
// }

// export default UserIntake;
