from jogoAdivinhacaoPOO import JogoAdivinhacao
import pytest

@pytest.fixture
def jogo():
    return JogoAdivinhacao();

def test_constructor(jogo):
    assert jogo.limite == 100;
    assert jogo.escolhaTentativas == 3;