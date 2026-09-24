const res = document.querySelector("#res");
const frm = document.querySelector("form");

const tituloInput = document.querySelector("#titulo");
const editoraInput = document.querySelector("#editora");
const statusInput = document.querySelector("#status");
const capaInput = document.querySelector("#capa");

frm.addEventListener("submit", async (event) => {
  event.preventDefault();
  res.innerHTML = "";

  const capa = capaInput.files[0];
  let imagem;

  if (!capa) {
    imagem = null;
  } else if (!capa.type.startsWith("image/")) {
    res.style.color = "red";
    res.innerHTML = "Arquivo nao é uma imagem";
    return;
  }

  try {
    imagem = await converterParaWebp(capa);
  } catch (error) {
    console.error(error);

    res.style.color = "red";
    res.innerHTML = "Arquivo nao é uma imagem";

    return;
  }

  await EnviarDados(imagem);
});

async function converterParaWebp(capa) {
  const imagem = new Image();
  imagem.src = URL.createObjectURL(capa);
  await imagem.decode();

  const canvas = document.createElement("canvas");
  canvas.width = imagem.width;
  canvas.height = imagem.height;

  const contexto = canvas.getContext("2d");
  contexto.drawImage(imagem, 0, 0);

  const webp = await new Promise((resolve) => {
    canvas.toBlob(resolve, "image/webp", 0.85);
  });

  URL.revokeObjectURL(imagem.src);

  return webp;
}

async function EnviarDados(imagem) {
  const dados = new FormData();

  dados.append("titulo", tituloInput.value);
  dados.append("editora", editoraInput.value);
  dados.append("status", statusInput.value);
  if (imagem) {
    dados.append("capa", imagem, "capa.webp");
  }

  const resposta = await fetch("https://listadeleituras.onrender.com/obras/", {
    method: "POST",
    body: dados,
  });

  const resultado = await resposta.json();

  if (resposta.ok) {
    res.style.color = "green";
    res.innerHTML = resultado.success;

    frm.reset();
  } else {
    res.style.color = "red";
    res.innerHTML = resultado.detail;
  }
}
