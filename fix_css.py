
css_content = r"""@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:ital,wght@0,500;1,900&display=swap');
*{
    font-family: 'Dancing Script', cursive;
}
/* body{
    color: azure;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: black;
} */
.greetings{
    position: absolute;
    top: 8%;
    left: 50%;
    transform: translateX(-50%);
    color: azure;
    font-size: 3rem;
    font-weight: 900;
    z-index: 2; 
    display: flex;
    flex-direction: row;
    gap: 10px;
    width: 100%;
    justify-content: center;
    text-align: center;
}
.greetings > span{
    animation: glow 2.5s ease-in-out infinite;
}
@keyframes glow{
    0%, 100%{
        color: #fff0f5; /* Lavender Blush */
        text-shadow: 0 0 12px #ff69b4, 0 0 50px #ff1493, 0 0 100px #ff007f;
    }
    10%, 90%{
        color: #ffb6c1; /* Light Pink */
        text-shadow: none;
    }
}
.greetings > span:nth-child(2){
    animation-delay: .2s ;
}
.greetings > span:nth-child(3){
    animation-delay: .4s ;
}
.greetings > span:nth-child(4){
    animation-delay: .6s;
}
.greetings > span:nth-child(5){
    animation-delay: .8s;
}

.description-container {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 5%;
    z-index: 100; 
    pointer-events: none; 
}

.description-left, .description-right {
    width: 25%;
    color: #ffd1dc; /* Pastel Pink */
    font-size: 1.5rem; /* Slightly larger for script font readability */
    background: rgba(50, 0, 20, 0.6); /* Darker reddish background for contrast */
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #ff69b4; /* Pink border */
    box-shadow: 0 0 15px rgba(255, 105, 180, 0.3);
}

.description-left {
    text-align: justify;
}

.description-right {
    text-align: justify;
}

.button {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translateX(-50%);
    z-index: 2; 
    background-color: #ff69b4; /* Hot Pink */
    padding: 10px 25px;
    border-radius: 25px;
    box-shadow: 0 0 10px #ff1493;
    animation: glow-button 2s infinite alternate;
}

@keyframes glow-button {
    from { box-shadow: 0 0 10px #ff1493; }
    to { box-shadow: 0 0 20px #ff69b4, 0 0 5px white; }
}

.button a{
    text-decoration: none;
    font-size: 1.2rem;
    color: white;
    font-weight: bold;
}

@media screen and (max-width: 574px) {
    .greetings {
        font-size: 2.5rem; 
        display: block;
        text-align: center;
        top: 25%; /* Move down towards the middle/flowers */
        width: 100%;
        line-height: 1.2;
    }
    
    .description-container {
        display: none; /* Hide the big text boxes on mobile */
    }

    .button {
        display: none; /* Hide the Explore button on mobile */
    }
    
    /* Show the mobile button */
    .mobile-open-message {
        display: block !important;
        position: absolute;
        bottom: 50%;
        left: 50%;
        transform: translateX(-50%);
        z-index: 200;
    }
}

/* Base styles for mobile elements (Hidden on desktop by default) */
.mobile-open-message {
    display: none;
}

#openMessageBtn {
    background-color: #ff69b4;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 30px;
    font-size: 1.2rem;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(255, 20, 147, 0.5);
    cursor: pointer;
    font-family: 'Dancing Script', cursive;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
    40% {transform: translateY(-10px);}
    60% {transform: translateY(-5px);}
}

/* Letter Overlay Styles */
.letter-overlay {
    display: none; /* Hidden by default */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    z-index: 1000;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.letter-content {
    background-image: linear-gradient(to bottom, #fff0f5, #ffe4e1);
    color: #8b0000;
    padding: 30px;
    border-radius: 10px;
    max-width: 90%;
    width: 400px;
    position: relative;
    box-shadow: 0 0 20px rgba(255, 105, 180, 0.6);
    text-align: center;
    border: 2px solid #ff69b4;
}

.letter-content h2 {
    font-family: 'Dancing Script', cursive;
    font-size: 2rem;
    margin-bottom: 20px;
    color: #ff1493;
}

.letter-content p {
    font-family: 'Poppins', sans-serif; /* Readable font for body text */
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 15px;
}

.close-btn {
    position: absolute;
    top: 10px;
    right: 15px;
    font-size: 1.5rem;
    cursor: pointer;
    color: #ff1493;
    font-weight: bold;
}

.overlay-start {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.9);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10000;
    transition: opacity 1s ease;
}

.overlay-content {
    text-align: center;
    color: white;
    font-family: 'Dancing Script', cursive;
    animation: pulse 2s infinite;
}

.overlay-content h1 {
    font-size: 3rem;
    margin-bottom: 20px;
}

.overlay-content p {
    font-size: 1.5rem;
}

@keyframes pulse {
    0% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(1); opacity: 0.8; }
}

.hidden {
    opacity: 0;
    pointer-events: none;
}
"""

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)
