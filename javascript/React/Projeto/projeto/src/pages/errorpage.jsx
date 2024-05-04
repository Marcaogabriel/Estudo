import React from "react";
import { useRouteError } from "react-router-dom";

export default function ErrorPage() {
  const erro = useRouteError();
  console.error(erro );

  return (
    <div
      style={{
        textAlign: "center",
        display: "flex", 
        alignItems: "center",
        justifyContent: "center",
        height: "100vh",
      }}
    >
    <div>
      <h1 style={{ color: "#ff002b",}} > Oops!</h1>  
        <div style={{color: "#ffffff"}}>
          <p>Desculpa, ocorreu um erro inesperado.</p>
          <p>{erro.status} - {erro.statusText || erro.message}</p>
        </div>
      </div>
    </div>
  );
}