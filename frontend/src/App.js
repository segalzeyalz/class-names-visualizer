import React, {useEffect, useState} from 'react';
import ReactWordcloud from 'react-wordcloud';
import axios from 'axios';
import { isEmpty } from 'lodash';
import { InfinitySpin } from 'react-loader-spinner';
import './app.css'

const App = () => {
    const [words, setWords] = useState([]);

    useEffect(() => {
        // Rate-limit for the site (batches)
        const fetchData = async () => {
            try {
                const { data } = await axios.get('http://127.0.0.1:5000/classNames?amount=100');
                const wordsToFill = Object.entries(data).map(([text, value]) => ({ text, value }));
                setWords(wordsToFill)
            } catch (error) {
                setWords([])
                console.error("Failed to fetch words from server:", error);
            }
        };

        return fetchData;
    }, []);

    return (
        <div className="word-cloud-container">
            {isEmpty(words) ?
                <InfinitySpin color="purple" /> :
                <ReactWordcloud words={words}/>
            }
        </div>
    );
};

export default App;
