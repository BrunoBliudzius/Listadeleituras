async function carregarObras() {
  try {
    const resposta = await fetch("https://listadeleituras.onrender.com/obras/");

    if (!resposta.ok) {
      throw new Error("Erro ao buscar obras");
    }

    const obras = await resposta.json();

    const tabela = document.querySelector("#tabela-obras");
    tabela.innerHTML = "";

    for (const obra of obras) {
      const linha = document.createElement("tr");

      // Se não houver capa, renderiza um placeholder bonito com ícone
      const capaHtml = obra.capa_url
        ? `<img src="https://listadeleituras.onrender.com${obra.capa_url}" alt="Capa de ${obra.titulo}" class="capa-img shadow-sm" />`
        : `<div class="bg-secondary-subtle d-flex align-items-center justify-content-center capa-img shadow-sm">
             <i class="bi bi-book text-secondary fs-4"></i>
           </div>`;

      // Tratamento de valores nulos para editora
      const editoraHtml = obra.editora
        ? obra.editora
        : '<span class="text-muted">Não informada</span>';

      linha.innerHTML = `
        <td class="ps-4">
            ${capaHtml}
        </td>

        <td>
            <h6 class="mb-0 fw-bold text-dark">${obra.titulo}</h6>
        </td>

        <td>
            ${editoraHtml}
        </td>

        <td>
            ${formatarStatus(obra.status)}
        </td>

        <td class="pe-4 text-end">
            <button class="btn btn-sm btn-outline-secondary rounded-circle" title="Editar" onclick="editarObra(${obra.id})">
                <i class="bi bi-pencil"></i>
            </button>
            <button class="btn btn-sm btn-outline-danger rounded-circle ms-1" title="Excluir" onclick="excluirObra(${obra.id})">
                <i class="bi bi-trash"></i>
            </button>
        </td>
      `;

      tabela.appendChild(linha);
    }
  } catch (erro) {
    console.error("Erro:", erro);

    //Mostrar uma mensagem de erro na tela para o usuário
    document.querySelector("#tabela-obras").innerHTML = `
      <tr>
        <td colspan="5" class="text-center text-danger py-4">
          <i class="bi bi-exclamation-triangle me-2"></i> Não foi possível carregar as obras. Verifique se o servidor está rodando.
        </td>
      </tr>
    `;
  }
}

// Função auxiliar para criar Badges coloridos dependendo do status
function formatarStatus(status) {
  if (!status) return '<span class="text-muted">-</span>';

  const statusLower = status.toLowerCase();

  if (statusLower.includes("lido")) {
    return `<span class="badge bg-success-subtle text-success border border-success-subtle rounded-pill px-3 py-2"><i class="bi bi-check-circle me-1"></i> ${status}</span>`;
  }
  if (statusLower.includes("lendo")) {
    return `<span class="badge bg-warning-subtle text-warning border border-warning-subtle rounded-pill px-3 py-2"><i class="bi bi-book-half me-1"></i> ${status}</span>`;
  }
  if (statusLower.includes("quero ler") || statusLower.includes("pendente")) {
    return `<span class="badge bg-info-subtle text-info border border-info-subtle rounded-pill px-3 py-2"><i class="bi bi-bookmark me-1"></i> ${status}</span>`;
  }
}

function editarObra(id) {
  console.log("Apertou editar");
}

function excluirObra(id) {
  console.log("Apertou excluir");
}

carregarObras();
